var ec_center = echarts.init(document.getElementById('r2'), "dark");

var mydata = [{'name': '上海', 'value': 2079}, {'name': '云南', 'value': 352}
                ,{'name': '西藏', 'value': 1}, {'name': '澳门', 'value': 51}
                ,{'name': '青海', 'value': 18}, {'name': '台湾', 'value': 6761}
                ,{'name': '香港', 'value': 11836}, {'name': '贵州', 'value': 147}
                , {'name': '吉林', 'value': 573}, {'name': '新疆', 'value': 980}
                , {'name': '宁夏', 'value': 76}, {'name': '内蒙古', 'value': 386}
                , {'name': '甘肃', 'value': 194}, {'name': '天津', 'value': 393}
                , {'name': '山西', 'value': 253}, {'name': '辽宁', 'value': 425}
                , {'name': '黑龙江', 'value': 1612}, {'name': '海南', 'value': 188}
                , {'name': '河北', 'value': 1317}, {'name': '陕西', 'value': 613}
                , {'name': '广西', 'value': 275}, {'name': '福建', 'value': 617}
                , {'name': '北京', 'value': 1059}, {'name': '江苏', 'value': 725}
                , {'name': '四川', 'value': 1019}, {'name': '山东', 'value': 883}
                , {'name': '江西', 'value': 937}, {'name': '重庆', 'value': 598}
                , {'name': '安徽', 'value': 1004}, {'name': '湖南', 'value': 1051}
                , {'name': '河南', 'value': 1314}, {'name': '广东', 'value': 2427}
                , {'name': '浙江', 'value': 1363}, {'name': '湖北', 'value': 68159}]

var ec_center_option = {
    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8
        },
        splitList: [{start: 1, end: 9},
            {start: 10, end: 99},
            {start: 100, end: 999},
            {start: 1000, end: 9999},
            {start: 10000}],
        color: ['#8A3310', '#c64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: '累计确诊人数',
        type: 'map',
        mapType: 'china',
        roam: false, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#009fe8', //区域边框颜色
                areaColor: "#ffefd5", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: "#ef3737",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8
            },
            emphasis: {
                show: true,
                fontSize: 8
            }
        },
        data: mydata //数据
    }]
};
ec_center.setOption(ec_center_option);