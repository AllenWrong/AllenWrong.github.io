---
title: "Paper-Search"
excerpt: ""
date: 2022-03-17 17:57:27
mathjax: false
---

<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
        <style>
            .results_table {
                border: 1px;
            }
        </style>
    </head>
​    <body>
​        <button value="点击" id="click_bt">点击</button>

        <center><div id="table"></div></center>

        <script>
            $.ajax({
                url: '../../../../A_paper_sets.csv',
                dataType: 'text',
            }).done(successFunction);
    
            function successFunction(data) {
                var allRows = data.split(/\r?\n|\r/);
                var table = "<table border='1' width='800' cellpadding='5' cellspacing='0'>";
                table += "<thead><tr>"
                table += "<th>会议/期刊</th>";
                table += "<th>论文</th></tr></thead><tbody>"
                for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
                    table += '<tr>';
                    var rowCells = allRows[singleRow].split(',');
                    for (var rowCell = 0; rowCell < rowCells.length; rowCell++) {
                        table += '<td>';
                        table += rowCells[rowCell];
                        table += '</td>';
                    }
                    table += '</tr>';
                } 
                table += '</tbody>';
                table += '</table>';
                $('#table').append(table);
            }
            $('#click_bt').click(function(){
                $.get("https://dblp.uni-trier.de/db/conf/sigmod/sigmod2021.html", function(data, status) {
                    console.log(`${data}`)
                })
            })
    
            const Url='https://www.baidu.com';
            axios.get(Url).then(data=>console.log(data)).catch(err=>console.log(err))
    
        </script>
    </body>
</html>