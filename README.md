# City Distance Calculator (城市距离计算器)
一个用于计算中国城市行政区与市中心距离的Python工具。
## 功能特点
- 支持多个主要城市的行政区距离计算
 使用Haversine公式计算真实地理距离
 支持CSV格式输出
 包含详细的城市行政区经纬度数据
## 安装依赖
```bash
pip install -r requirements.txt
```

```bash
python examples/basic_usage.py
```
## 支持的城市

目前支持以下城市的距离计算：
- 上海市
- 杭州市
- 宁波市
- 温州市
- 金华市
- 郑州市
- 安阳市
- 武汉市
- 长沙市
- 西安市
- 合肥市
- 滁州市
- 宜春市
- 南昌市
- 洛阳市
- 绍兴市

## 数据格式

生成的CSV文件包含以下字段：
- 城市：城市名称
- 行政区：行政区名称
- 行政区纬度：行政区的纬度坐标
- 行政区经度：行政区的经度坐标
- 市中心纬度：计算得出的市中心纬度
- 市中心经度：计算得出的市中心经度
- 市中心距离(公里)：行政区到市中心的距离

## 贡献指南

欢迎提交 Pull Request 来帮助改进项目。以下是贡献步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 开源协议

本项目采用 MIT 协议 - 详见 [LICENSE](LICENSE) 文件

