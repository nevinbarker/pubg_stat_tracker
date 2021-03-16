document.getElementById('graph_sel').addEventListener('change', function() {
    var graphSelector = document.getElementById("graph_sel").value
    console.log(graphSelector)
        if (graphSelector === '1') {
            document.getElementById("graphDiv").className = "container mt-3 mb-3"
            document.getElementById("graph").src = `data:image/jpg;base64, ${graphKillsPerMatch}`
        }
        else if (graphSelector === '2') {
            document.getElementById("graphDiv").className = "container mt-3 mb-3"
            document.getElementById("graph").src = `data:image/jpg;base64, ${graphDmgPerMatch}`
        }
        else if (graphSelector === '3') {
            document.getElementById("graphDiv").className = "container mt-3 mb-3"
            document.getElementById("graph").src = `data:image/jpg;base64, ${graphTimeAlivePerMatch}`
        }
})


console.log('pls')