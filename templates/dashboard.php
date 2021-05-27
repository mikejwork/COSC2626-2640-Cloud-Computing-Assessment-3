{% extends 'template.php' %}


{% block head %}

<title>portfol.io - dashboard</title>

{% endblock %}



{% block body %}
    <section style="padding: 15%;font-family: Ubuntu, sans-serif;border-top: 1px inset rgba(255,255,255,0.07);padding-top: 0px;">
        <div class="container" style="color: rgb(255,255,255);padding: 2%;background: rgba(18,18,18,0);border-radius: 15px;font-family: Roboto, sans-serif;padding-bottom: 0px;padding-left: 10%;padding-right: 10%;">
            <div style="margin-bottom: 5%;">
                <h1 style="font-weight: normal;font-style: normal;font-family: Ubuntu, sans-serif;margin-bottom: 5px;">my dashboard</h1>
                <p style="color: rgba(255,255,255,0.5);">View your positions and current portfolio balance below. You can also view the most popular stocks being purchased by our userbase.</p>
            </div>
        </div>
        <div class="container">
            <div class="row g-0 d-xxl-flex justify-content-center align-items-center align-items-xxl-center">

                <div class="col-auto col-md-3" style="color: rgba(255,255,255,0.85);background: #191919DD;font-family: Ubuntu, sans-serif;border-radius: 10px;padding: 15px;padding-right: 15px;padding-left: 15px;margin-right: 5px;margin-bottom: 5px;">
                    <div style="display: flex;margin-bottom: 5px;">
                        <p style="margin-bottom: 0px;">BTC $ AUD<i class="fa fa-question-circle" style="margin-left: 5px;"></i></p>
                        <div style="width: auto;background: #0e0e0e;display: inline-block;border-radius: 20px;padding-right: 12px;padding-left: 12px;margin-left: auto;">
                            <p style="margin-bottom: 0px;color: rgba(224,48,24,0.85);"><i class="fa fa-long-arrow-down" style="margin-right: 5px;"></i>-12.45%</p>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 5px;">
                        <p style="margin-bottom: 0px;color: rgba(48,105,217,0.85);"><strong>68.54%</strong></p>
                        <div style="width: auto;background: rgba(14,14,14,0);display: inline-block;border-radius: 20px;padding-right: 12px;padding-left: 12px;margin-left: auto;">
                            <p style="margin-bottom: 0px;color: rgb(71,71,71);border-color: rgb(18,18,18);"><strong>$42,201.37</strong></p>
                        </div>
                    </div>
                    <div id="chart" style="margin: 0px;height: 100px;"></div>
                </div>
                

                <div class="col-auto col-md-3" style="color: rgba(255,255,255,0.85);background: #191919;font-family: Ubuntu, sans-serif;border-radius: 10px;padding: 15px;padding-right: 15px;padding-left: 15px;margin-right: 5px;margin-bottom: 5px;">
                    <div style="display: flex;margin-bottom: 5px;">
                        <p style="margin-bottom: 0px;">Add a new position</p>
                    </div>
                    <div style="display: flex;margin-bottom: 5px;">
                        <p style="margin-bottom: 0px;color: rgba(255,255,255,0.5);">Enter the stock information below</p>
                    </div>
                    <div style="margin: 0px;height: 100px;">
                        <form><input class="form-control" type="text" style="width: 100%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 5px;font-size: 12px;" placeholder="Stock code"><input class="form-control" type="text" style="width: 100%;background: rgb(16,16,16);font-family: Ubuntu, sans-serif;border-width: 1px;border-color: rgb(27,28,28);color: rgb(255,255,255);border-top-right-radius: 0px;border-bottom-right-radius: 0px;margin-bottom: 5px;font-size: 12px;" placeholder="Amount owned"><button class="btn btn-primary" type="button" style="font-size: 12px;width: 100%;padding-top: 3px;padding-bottom: 3px;background: rgb(16,16,16);border-color: rgb(27,28,28);">Add</button></form>
                    </div>
                </div>
                
            </div>
        </div>


        <div class="container" style="color: rgb(255,255,255);padding: 2%;background: rgba(18,18,18,0);border-radius: 15px;font-family: Roboto, sans-serif;padding-bottom: 0px;padding-left: 10%;padding-right: 10%;">
            <div style="margin-bottom: 5%;">
                <h1 style="font-weight: normal;font-style: normal;font-family: Ubuntu, sans-serif;margin-bottom: 5px;">user insight</h1>
                <p style="color: rgba(255,255,255,0.5);">View the most popular stocks being purchased by our userbase.</p>
            </div>
        </div>
        <div class="container">
            <div class="row g-0 d-xxl-flex justify-content-center align-items-center align-items-xxl-center">
                
                <div class="col-auto col-md-3" style="color: rgba(255,255,255,0.85);background: #191919DD;font-family: Ubuntu, sans-serif;border-radius: 10px;padding: 15px;padding-right: 15px;padding-left: 15px;margin-right: 5px;margin-bottom: 5px;">
                    <div style="display: flex;margin-bottom: 5px;">
                        <p style="margin-bottom: 0px;">BTC $ AUD<i class="fa fa-question-circle" style="margin-left: 5px;"></i></p>
                        <div style="width: auto;background: #0e0e0e;display: inline-block;border-radius: 20px;padding-right: 12px;padding-left: 12px;margin-left: auto;">
                            <p style="margin-bottom: 0px;color: rgba(40,224,24,0.85);"><i class="fa fa-long-arrow-up" style="margin-right: 5px;"></i>24hr Highest mover</p>
                        </div>
                    </div>
                    <div style="display: flex;margin-bottom: 5px;">
                        <p style="margin-bottom: 0px;color: rgba(48,105,217,0.85);"><br></p>
                        <div style="width: auto;background: rgba(14,14,14,0);display: inline-block;border-radius: 20px;padding-right: 12px;padding-left: 12px;margin-left: auto;">
                            <p style="margin-bottom: 0px;color: rgb(71,71,71);border-color: rgb(18,18,18);"><strong>$48,238.80</strong></p>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </section>

<script>
    var options = {
        chart: {
            type: 'area',
            zoom: {
                enabled: false
            },
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: false
            }
        },
        series: [{
            name: 'BTC $ AUD',
            data: [123, 22, 313, 322, 311, 266, 255, 244, 277, 322, 255, 155]
        }],
        dataLabels: {
            enabled: false
        },
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        grid: {
            show: false
        },
        xaxis: {
            labels: {
                show: false
            }
        },
        yaxis: {
            opposite: true,
            labels: {
                show: true
            }
        },
        tooltip: {
            enabled: true,
            theme: "dark",
            x: {
                show: false
            }
        }
    }
    var chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();
</script>
{% endblock %}