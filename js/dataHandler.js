/**
 * 通过jsonp读取到json文件中处理后的数据
 * 回调函数，名需要与 src 中一致，而且要与文件地址中名一致。jsonp格式 名称({}) 不然无法获取到对应的文件
 * @param {*} result 
 */
function loadLineChartData(result){
    
     initLine(result)
}

/**
 * 通过jsonp读取到json文件中处理后的数据
 * 回调函数，名称需要与 src 中一致，而且要与文件地址中名一致。jsonp格式 名称({}) 不然无法获取到对应的文件
 * @param {*} result 
 */
function loadNetData(result){
    
    initNet(result)
}

/**
 * 根据传入数据，初始化折线图
 * @param {*} webkitDep 
 */
function initLine(webkitDep) {
    var lineChart = echarts.init(document.getElementById('linebox'));
    let option = {
        title: {
            text: "标题",
            x: 'center'
        },
        grid: {
            bottom: 80
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type : 'line'
            }
        },
        dataZoom: [
            {
                type: 'slider',
                xAxisIndex: 0,
                filterMode: 'empty'
            },
            {
                type: 'inside',
                xAxisIndex: 0,
                filterMode: 'empty'
            }
        ],
        xAxis: {
            data: webkitDep.timeList
        },
        yAxis : [{
            name: "次数",
            type : 'value',
        }],
        series: [{
            data: webkitDep.yCountList,
            type: 'line'
        }]
    };
    lineChart.setOption(option);
}

/**
 * 根据传入数据，初始化关系网络图
 * @param {*} webkitDep 
 */
function initNet(webkitDep) {
    var netChart = echarts.init(document.getElementById('netbox'));

    let option = {
        legend: {
            data: ['rawUser']
        },
        series: [{
            type: 'graph',
            layout: 'force',
            animation: false,
            label: {
                normal: {
                    position: 'right',
                    formatter: '{b}'
                }
            },
            animationDurationUpdate: 1500,
            animationEasingUpdate: 'quinticInOut',
            draggable: false,
            data: webkitDep.nodes.map(function (node, idx) {
                return node;
            }),
            categories: webkitDep.categories,
            force: {
                edgeLength: 3,
                repulsion: 10,
                gravity: 0.2,
                layoutAnimation: false
            },
            edges: webkitDep.links
        }]
    };
    netChart.setOption(option);
}