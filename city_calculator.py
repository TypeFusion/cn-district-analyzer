import pandas as pd
from math import radians, sin, cos, sqrt, atan2
from typing import Dict, List, Tuple
from city_districts_data import CITY_DISTRICTS

class LocalDataSource:
    def __init__(self, city_data: Dict):
        self.city_data = city_data

    def get_city_center(self, city_name: str) -> Tuple[float, float]:
        """获取城市中心点坐标（使用所有行政区的平均值）"""
        if city_name not in self.city_data:
            print(f"未找到{city_name}的数据")
            return None

        districts = self.city_data[city_name]
        if not districts:
            return None

        avg_lat = sum(d['lat'] for d in districts) / len(districts)
        avg_lon = sum(d['lon'] for d in districts) / len(districts)
        return (avg_lat, avg_lon)

    def get_districts(self, city_name: str) -> List[Dict]:
        """获取城市的行政区数据"""
        return self.city_data.get(city_name, [])

class CityDistanceCalculator:
    def __init__(self, data_source: LocalDataSource):
        self.data_source = data_source

    def haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """计算两个坐标点之间的距离（公里）"""
        R = 6371  # 地球平均半径（公里）

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        return round(distance, 2)

    def calculate_city_distances(self, city_name: str) -> pd.DataFrame:
        """计算城市中心到各个行政区的距离"""
        city_center = self.data_source.get_city_center(city_name)
        if not city_center:
            print(f"错误: 无法获取{city_name}的中心点坐标")
            return pd.DataFrame()

        districts = self.data_source.get_districts(city_name)
        if not districts:
            print(f"警告: 未找到{city_name}的行政区数据")
            return pd.DataFrame()

        distances = []
        for district in districts:
            distance = self.haversine_distance(
                city_center[0], city_center[1],
                district['lat'], district['lon']
            )

            distances.append({
                "城市": city_name,
                "行政区": district['name'],
                "行政区纬度": district['lat'],
                "行政区经度": district['lon'],
                "市中心纬度": city_center[0],  # 添加市中心坐标
                "市中心经度": city_center[1],  # 添加市中心坐标
                "市中心距离(公里)": distance
            })

        df = pd.DataFrame(distances)
        print(f"成功获取{city_name}的{len(distances)}个行政区数据")
        return df

    def process_all_cities(self, cities: List[str], output_file: str = "city_distances.csv"):
        """处理所有城市并生成CSV文件"""
        all_distances = []
        failed_cities = []

        for city in cities:
            print(f"\n处理城市: {city}")
            df = self.calculate_city_distances(city)
            if not df.empty:
                all_distances.append(df)
            else:
                failed_cities.append(city)

        if all_distances:
            final_df = pd.concat(all_distances, ignore_index=True)
            # 按城市和距离排序
            final_df = final_df.sort_values(['城市', '市中心距离(公里)'])
            final_df.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"\n数据已保存到: {output_file}")
            print(f"成功处理的城市数量: {len(all_distances)}")
            print(f"总行政区数量: {len(final_df)}")

        if failed_cities:
            print(f"\n以下城市处理失败: {', '.join(failed_cities)}")
