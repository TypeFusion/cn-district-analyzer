from city_calculator import LocalDataSource, CityDistanceCalculator
from city_districts_data import CITY_DISTRICTS

# 创建数据源和计算器实例
data_source = LocalDataSource(CITY_DISTRICTS)
calculator = CityDistanceCalculator(data_source)

# 要处理的城市列表
cities = [
    "上海市", "杭州市", "宁波市", "温州市", "金华市", 
    "郑州市", "安阳市", "武汉市", "长沙市", "西安市", 
    "合肥市", "滁州市", "宜春市", "南昌市", "洛阳市", 
    "绍兴市"
]

# 处理所有城市
calculator.process_all_cities(cities, "city_districts_distances.csv")