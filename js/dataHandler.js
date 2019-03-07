$(() => {
    // initNetData()
})


function loadLineChartData(result){
    //回调函数名称(indexDemo)，需要与 src 中一致，而且要与文件地址中名一致。jsonp格式 名称({})
  //不然无法获取到对应的文件
     console.log(result)     //打印 indexDemo.json 中的数据
     initNet(result)
}

function loadNetData(webkitDep){
    //回调函数名称(indexDemo)，需要与 src 中一致，而且要与文件地址中名一致。jsonp格式 名称({})
  //不然无法获取到对应的文件
    //  console.log(result)     //打印 indexDemo.json 中的数据
     
}

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
            draggable: true,
            data: webkitDep.nodes.map(function (node, idx) {
                // node.id = idx;
                return node;
            }),
            categories: webkitDep.categories,
            force: {
                // initLayout: 'circular'
                // repulsion: 20,
                edgeLength: 5,
                repulsion: 20,
                gravity: 0.2
            },
            edges: webkitDep.links
        }]
    };

    netChart.setOption(option);
}