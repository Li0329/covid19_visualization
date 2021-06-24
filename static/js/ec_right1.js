var ec_right1 = echarts.init(document.getElementById('r1'), "dark");

var ec_right1_Option = {
	title: {
        text: '世界各洲确诊人数占比',
    },
    legend: {
        top: 'bottom'
    },
    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series: [
        {
            name: '各洲确诊人数',
            type: 'pie',
            radius: [25, 125],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
                borderRadius: 6
            },
            data: [
                {value: 4781880, name: '非洲'},
                {value: 39426984, name: '北美洲'},
                {value: 67219, name: '大洋洲'},
                {value: 27500022, name: '南美洲'},
                {value: 46118440, name: '欧洲'},
                {value: 48508461, name: '亚洲'}
            ]
        }
    ]
};

ec_right1.setOption(ec_right1_Option);