# OpenCSG StarShip CodeGenAgent introduction

OpenCSG StarShip is a digital employee platform developed by OpenCSG and all digital employees are built up with LLM and AI Agents. 
One of the core agents is OpenCSG StarShip CodeGenAgent, which provides full e2e issue2code function.

OpenCSG StarShip CodeGenAgent Features:
- GitOps workflow design with no need for IDE and manual intervention
- Automated code generation to complete issue2code tasks
- Customized software programming AI Agent design following the process of requirement understanding, task planning, code design, and code writing
- Support for integration with multiple OpenAI-compatible LLM formats
- Code repository understanding and search based on vector retrieval and AST technology

OpenCSG StarShip CodeGenAgent SWEBench Test info:
We use OpenCSG StarShip CodeGenAgent(v2024-05) with Azure GPT-4(version:0125-Preview) for this test.
Our test result runs on SWEBench Lite with 300 case

Tech detail of StarShip LLM agent's design is on the way.
For product details and trial access, please visit: https://opencsg.com/product?class=StarShip

# Benchmark results

## Patch Apply Success

| Resolved | Count | Rate |
| -------- | ----- | ---- |
| Yes | 71 | 23.91% |
| Partially | 9 | 3.03% |
| No | 217 | 73.06% |  


## Patch Apply Success + Failure

| Resolved | Count | Rate |
| -------- | ----- | ---- |
| Yes | 71 | 23.67% |
| Partially | 9 | 3.0% |
| No | 220 | 73.33% |  


## Benchmark instances

### Generated but not applied

| Instance ID | Repository | Testbed version |
| ----------- | ---------- | --------------- |
| [django__django-11564](logs/django__django-11564.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-15738](logs/django__django-15738.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |


### Applied but not resolved

| Instance ID | Repository | Testbed version |
| ----------- | ---------- | --------------- |
| [astropy__astropy-12907](logs/astropy__astropy-12907.20240524_opencsg_starship_gpt4.eval.log) | astropy/astropy | 4.3 |
| [astropy__astropy-14182](logs/astropy__astropy-14182.20240524_opencsg_starship_gpt4.eval.log) | astropy/astropy | 5.1 |
| [astropy__astropy-14365](logs/astropy__astropy-14365.20240524_opencsg_starship_gpt4.eval.log) | astropy/astropy | 5.1 |
| [astropy__astropy-6938](logs/astropy__astropy-6938.20240524_opencsg_starship_gpt4.eval.log) | astropy/astropy | 1.3 |
| [astropy__astropy-7746](logs/astropy__astropy-7746.20240524_opencsg_starship_gpt4.eval.log) | astropy/astropy | 1.3 |
| [django__django-10924](logs/django__django-10924.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11019](logs/django__django-11019.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11099](logs/django__django-11099.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11283](logs/django__django-11283.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11422](logs/django__django-11422.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11620](logs/django__django-11620.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11630](logs/django__django-11630.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11742](logs/django__django-11742.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11797](logs/django__django-11797.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-11815](logs/django__django-11815.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-11848](logs/django__django-11848.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-11905](logs/django__django-11905.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-11910](logs/django__django-11910.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-11964](logs/django__django-11964.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12113](logs/django__django-12113.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12125](logs/django__django-12125.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12184](logs/django__django-12184.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12284](logs/django__django-12284.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12308](logs/django__django-12308.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12470](logs/django__django-12470.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12497](logs/django__django-12497.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12589](logs/django__django-12589.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12700](logs/django__django-12700.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12708](logs/django__django-12708.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12747](logs/django__django-12747.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12856](logs/django__django-12856.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-12908](logs/django__django-12908.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-12915](logs/django__django-12915.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13028](logs/django__django-13028.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13033](logs/django__django-13033.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13158](logs/django__django-13158.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13220](logs/django__django-13220.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13265](logs/django__django-13265.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13321](logs/django__django-13321.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13401](logs/django__django-13401.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13447](logs/django__django-13447.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-13448](logs/django__django-13448.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13551](logs/django__django-13551.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13660](logs/django__django-13660.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13710](logs/django__django-13710.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-13757](logs/django__django-13757.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13768](logs/django__django-13768.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13925](logs/django__django-13925.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-13964](logs/django__django-13964.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14155](logs/django__django-14155.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14238](logs/django__django-14238.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14411](logs/django__django-14411.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14534](logs/django__django-14534.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14608](logs/django__django-14608.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14667](logs/django__django-14667.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14730](logs/django__django-14730.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14787](logs/django__django-14787.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-14997](logs/django__django-14997.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-14999](logs/django__django-14999.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15061](logs/django__django-15061.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15202](logs/django__django-15202.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15213](logs/django__django-15213.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15252](logs/django__django-15252.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15320](logs/django__django-15320.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15388](logs/django__django-15388.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15400](logs/django__django-15400.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15695](logs/django__django-15695.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15781](logs/django__django-15781.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-15790](logs/django__django-15790.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-15819](logs/django__django-15819.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-15902](logs/django__django-15902.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-15996](logs/django__django-15996.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16046](logs/django__django-16046.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16229](logs/django__django-16229.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16400](logs/django__django-16400.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16408](logs/django__django-16408.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-16816](logs/django__django-16816.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-16820](logs/django__django-16820.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-16910](logs/django__django-16910.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-17051](logs/django__django-17051.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-17087](logs/django__django-17087.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [matplotlib__matplotlib-18869](logs/matplotlib__matplotlib-18869.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.3 |
| [matplotlib__matplotlib-22711](logs/matplotlib__matplotlib-22711.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-22835](logs/matplotlib__matplotlib-22835.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-23299](logs/matplotlib__matplotlib-23299.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-23314](logs/matplotlib__matplotlib-23314.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-23476](logs/matplotlib__matplotlib-23476.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-23562](logs/matplotlib__matplotlib-23562.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-23563](logs/matplotlib__matplotlib-23563.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.5 |
| [matplotlib__matplotlib-23913](logs/matplotlib__matplotlib-23913.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-23987](logs/matplotlib__matplotlib-23987.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-24149](logs/matplotlib__matplotlib-24149.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-24265](logs/matplotlib__matplotlib-24265.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-24334](logs/matplotlib__matplotlib-24334.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-24970](logs/matplotlib__matplotlib-24970.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-25079](logs/matplotlib__matplotlib-25079.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [matplotlib__matplotlib-25311](logs/matplotlib__matplotlib-25311.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [matplotlib__matplotlib-25332](logs/matplotlib__matplotlib-25332.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [matplotlib__matplotlib-25433](logs/matplotlib__matplotlib-25433.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [matplotlib__matplotlib-25442](logs/matplotlib__matplotlib-25442.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [matplotlib__matplotlib-25498](logs/matplotlib__matplotlib-25498.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [matplotlib__matplotlib-26011](logs/matplotlib__matplotlib-26011.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [matplotlib__matplotlib-26020](logs/matplotlib__matplotlib-26020.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.7 |
| [mwaskom__seaborn-2848](logs/mwaskom__seaborn-2848.20240524_opencsg_starship_gpt4.eval.log) | mwaskom/seaborn | 0.12 |
| [mwaskom__seaborn-3407](logs/mwaskom__seaborn-3407.20240524_opencsg_starship_gpt4.eval.log) | mwaskom/seaborn | 0.13 |
| [pallets__flask-4045](logs/pallets__flask-4045.20240524_opencsg_starship_gpt4.eval.log) | pallets/flask | 2.0 |
| [pallets__flask-4992](logs/pallets__flask-4992.20240524_opencsg_starship_gpt4.eval.log) | pallets/flask | 2.3 |
| [pallets__flask-5063](logs/pallets__flask-5063.20240524_opencsg_starship_gpt4.eval.log) | pallets/flask | 2.3 |
| [psf__requests-1963](logs/psf__requests-1963.20240524_opencsg_starship_gpt4.eval.log) | psf/requests | 2.3 |
| [psf__requests-2148](logs/psf__requests-2148.20240524_opencsg_starship_gpt4.eval.log) | psf/requests | 2.3 |
| [pydata__xarray-3364](logs/pydata__xarray-3364.20240524_opencsg_starship_gpt4.eval.log) | pydata/xarray | 0.12 |
| [pydata__xarray-4094](logs/pydata__xarray-4094.20240524_opencsg_starship_gpt4.eval.log) | pydata/xarray | 0.12 |
| [pydata__xarray-4248](logs/pydata__xarray-4248.20240524_opencsg_starship_gpt4.eval.log) | pydata/xarray | 0.12 |
| [pydata__xarray-4493](logs/pydata__xarray-4493.20240524_opencsg_starship_gpt4.eval.log) | pydata/xarray | 0.12 |
| [pylint-dev__pylint-5859](logs/pylint-dev__pylint-5859.20240524_opencsg_starship_gpt4.eval.log) | pylint-dev/pylint | 2.13 |
| [pylint-dev__pylint-6506](logs/pylint-dev__pylint-6506.20240524_opencsg_starship_gpt4.eval.log) | pylint-dev/pylint | 2.14 |
| [pylint-dev__pylint-7080](logs/pylint-dev__pylint-7080.20240524_opencsg_starship_gpt4.eval.log) | pylint-dev/pylint | 2.15 |
| [pylint-dev__pylint-7114](logs/pylint-dev__pylint-7114.20240524_opencsg_starship_gpt4.eval.log) | pylint-dev/pylint | 2.15 |
| [pylint-dev__pylint-7228](logs/pylint-dev__pylint-7228.20240524_opencsg_starship_gpt4.eval.log) | pylint-dev/pylint | 2.15 |
| [pylint-dev__pylint-7993](logs/pylint-dev__pylint-7993.20240524_opencsg_starship_gpt4.eval.log) | pylint-dev/pylint | 2.15 |
| [pytest-dev__pytest-5103](logs/pytest-dev__pytest-5103.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 4.5 |
| [pytest-dev__pytest-5221](logs/pytest-dev__pytest-5221.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 4.4 |
| [pytest-dev__pytest-5413](logs/pytest-dev__pytest-5413.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 4.6 |
| [pytest-dev__pytest-5495](logs/pytest-dev__pytest-5495.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 4.6 |
| [pytest-dev__pytest-6116](logs/pytest-dev__pytest-6116.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 5.2 |
| [pytest-dev__pytest-7168](logs/pytest-dev__pytest-7168.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 5.4 |
| [pytest-dev__pytest-7220](logs/pytest-dev__pytest-7220.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 5.4 |
| [pytest-dev__pytest-7432](logs/pytest-dev__pytest-7432.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 5.4 |
| [pytest-dev__pytest-7490](logs/pytest-dev__pytest-7490.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 6.0 |
| [pytest-dev__pytest-8365](logs/pytest-dev__pytest-8365.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 6.3 |
| [pytest-dev__pytest-8906](logs/pytest-dev__pytest-8906.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 7.0 |
| [pytest-dev__pytest-9359](logs/pytest-dev__pytest-9359.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 7.0 |
| [scikit-learn__scikit-learn-10297](logs/scikit-learn__scikit-learn-10297.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.20 |
| [scikit-learn__scikit-learn-10508](logs/scikit-learn__scikit-learn-10508.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.20 |
| [scikit-learn__scikit-learn-10949](logs/scikit-learn__scikit-learn-10949.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.20 |
| [scikit-learn__scikit-learn-11040](logs/scikit-learn__scikit-learn-11040.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.20 |
| [scikit-learn__scikit-learn-11281](logs/scikit-learn__scikit-learn-11281.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.20 |
| [scikit-learn__scikit-learn-12471](logs/scikit-learn__scikit-learn-12471.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [scikit-learn__scikit-learn-13241](logs/scikit-learn__scikit-learn-13241.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [scikit-learn__scikit-learn-13497](logs/scikit-learn__scikit-learn-13497.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [scikit-learn__scikit-learn-13779](logs/scikit-learn__scikit-learn-13779.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-14087](logs/scikit-learn__scikit-learn-14087.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-14092](logs/scikit-learn__scikit-learn-14092.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-14894](logs/scikit-learn__scikit-learn-14894.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-14983](logs/scikit-learn__scikit-learn-14983.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-15512](logs/scikit-learn__scikit-learn-15512.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-15535](logs/scikit-learn__scikit-learn-15535.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.22 |
| [scikit-learn__scikit-learn-25500](logs/scikit-learn__scikit-learn-25500.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 1.3 |
| [scikit-learn__scikit-learn-25570](logs/scikit-learn__scikit-learn-25570.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 1.3 |
| [scikit-learn__scikit-learn-25638](logs/scikit-learn__scikit-learn-25638.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 1.3 |
| [scikit-learn__scikit-learn-25747](logs/scikit-learn__scikit-learn-25747.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 1.3 |
| [sphinx-doc__sphinx-10451](logs/sphinx-doc__sphinx-10451.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 5.1 |
| [sphinx-doc__sphinx-11445](logs/sphinx-doc__sphinx-11445.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 7.1 |
| [sphinx-doc__sphinx-7686](logs/sphinx-doc__sphinx-7686.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.1 |
| [sphinx-doc__sphinx-7738](logs/sphinx-doc__sphinx-7738.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.1 |
| [sphinx-doc__sphinx-7975](logs/sphinx-doc__sphinx-7975.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.2 |
| [sphinx-doc__sphinx-8273](logs/sphinx-doc__sphinx-8273.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.3 |
| [sphinx-doc__sphinx-8282](logs/sphinx-doc__sphinx-8282.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.3 |
| [sphinx-doc__sphinx-8435](logs/sphinx-doc__sphinx-8435.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.4 |
| [sphinx-doc__sphinx-8474](logs/sphinx-doc__sphinx-8474.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.4 |
| [sphinx-doc__sphinx-8506](logs/sphinx-doc__sphinx-8506.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.4 |
| [sphinx-doc__sphinx-8627](logs/sphinx-doc__sphinx-8627.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.5 |
| [sphinx-doc__sphinx-8801](logs/sphinx-doc__sphinx-8801.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.5 |
| [sympy__sympy-11400](logs/sympy__sympy-11400.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-11870](logs/sympy__sympy-11870.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-11897](logs/sympy__sympy-11897.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-12171](logs/sympy__sympy-12171.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-12236](logs/sympy__sympy-12236.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-12419](logs/sympy__sympy-12419.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-12454](logs/sympy__sympy-12454.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-12481](logs/sympy__sympy-12481.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.0 |
| [sympy__sympy-13031](logs/sympy__sympy-13031.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13043](logs/sympy__sympy-13043.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13146](logs/sympy__sympy-13146.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13177](logs/sympy__sympy-13177.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13437](logs/sympy__sympy-13437.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13773](logs/sympy__sympy-13773.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13895](logs/sympy__sympy-13895.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13915](logs/sympy__sympy-13915.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-14024](logs/sympy__sympy-14024.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-14308](logs/sympy__sympy-14308.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-14396](logs/sympy__sympy-14396.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-15308](logs/sympy__sympy-15308.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-15345](logs/sympy__sympy-15345.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-15346](logs/sympy__sympy-15346.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-15609](logs/sympy__sympy-15609.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-15678](logs/sympy__sympy-15678.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-16106](logs/sympy__sympy-16106.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-16281](logs/sympy__sympy-16281.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.4 |
| [sympy__sympy-16503](logs/sympy__sympy-16503.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-16792](logs/sympy__sympy-16792.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-16988](logs/sympy__sympy-16988.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-17022](logs/sympy__sympy-17022.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-17139](logs/sympy__sympy-17139.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-17630](logs/sympy__sympy-17630.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-17655](logs/sympy__sympy-17655.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.5 |
| [sympy__sympy-18087](logs/sympy__sympy-18087.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-18189](logs/sympy__sympy-18189.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-18199](logs/sympy__sympy-18199.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-18532](logs/sympy__sympy-18532.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-18621](logs/sympy__sympy-18621.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-18698](logs/sympy__sympy-18698.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-18835](logs/sympy__sympy-18835.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-19007](logs/sympy__sympy-19007.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-19254](logs/sympy__sympy-19254.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.7 |
| [sympy__sympy-19487](logs/sympy__sympy-19487.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.7 |
| [sympy__sympy-20049](logs/sympy__sympy-20049.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.7 |
| [sympy__sympy-20322](logs/sympy__sympy-20322.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.8 |
| [sympy__sympy-20442](logs/sympy__sympy-20442.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.8 |
| [sympy__sympy-20590](logs/sympy__sympy-20590.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.7 |
| [sympy__sympy-20639](logs/sympy__sympy-20639.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.8 |
| [sympy__sympy-21055](logs/sympy__sympy-21055.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.8 |
| [sympy__sympy-21171](logs/sympy__sympy-21171.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.8 |
| [sympy__sympy-21379](logs/sympy__sympy-21379.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.9 |
| [sympy__sympy-21612](logs/sympy__sympy-21612.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.9 |
| [sympy__sympy-21614](logs/sympy__sympy-21614.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.9 |
| [sympy__sympy-21627](logs/sympy__sympy-21627.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.9 |
| [sympy__sympy-21847](logs/sympy__sympy-21847.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.9 |
| [sympy__sympy-22005](logs/sympy__sympy-22005.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.9 |
| [sympy__sympy-22714](logs/sympy__sympy-22714.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.10 |
| [sympy__sympy-22840](logs/sympy__sympy-22840.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.10 |
| [sympy__sympy-23191](logs/sympy__sympy-23191.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.11 |
| [sympy__sympy-24066](logs/sympy__sympy-24066.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.12 |
| [sympy__sympy-24102](logs/sympy__sympy-24102.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.12 |
| [sympy__sympy-24213](logs/sympy__sympy-24213.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.12 |
| [sympy__sympy-24909](logs/sympy__sympy-24909.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.13 |


### Resolved

| Instance ID | Repository | Testbed version |
| ----------- | ---------- | --------------- |
| [astropy__astropy-14995](logs/astropy__astropy-14995.20240524_opencsg_starship_gpt4.eval.log) | astropy/astropy | 5.2 |
| [django__django-10914](logs/django__django-10914.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11001](logs/django__django-11001.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11039](logs/django__django-11039.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11049](logs/django__django-11049.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11133](logs/django__django-11133.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11179](logs/django__django-11179.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11583](logs/django__django-11583.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.0 |
| [django__django-11999](logs/django__django-11999.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12286](logs/django__django-12286.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12453](logs/django__django-12453.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.1 |
| [django__django-12983](logs/django__django-12983.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13230](logs/django__django-13230.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13315](logs/django__django-13315.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13590](logs/django__django-13590.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13658](logs/django__django-13658.20240524_opencsg_starship_gpt4.eval.log) | django/django | 3.2 |
| [django__django-13933](logs/django__django-13933.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14016](logs/django__django-14016.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14017](logs/django__django-14017.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14382](logs/django__django-14382.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14580](logs/django__django-14580.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14672](logs/django__django-14672.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14752](logs/django__django-14752.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14855](logs/django__django-14855.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.0 |
| [django__django-14915](logs/django__django-14915.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15347](logs/django__django-15347.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15498](logs/django__django-15498.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.1 |
| [django__django-15789](logs/django__django-15789.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-15814](logs/django__django-15814.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-15851](logs/django__django-15851.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16041](logs/django__django-16041.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16139](logs/django__django-16139.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16255](logs/django__django-16255.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16379](logs/django__django-16379.20240524_opencsg_starship_gpt4.eval.log) | django/django | 4.2 |
| [django__django-16527](logs/django__django-16527.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-16595](logs/django__django-16595.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [django__django-16873](logs/django__django-16873.20240524_opencsg_starship_gpt4.eval.log) | django/django | 5.0 |
| [matplotlib__matplotlib-23964](logs/matplotlib__matplotlib-23964.20240524_opencsg_starship_gpt4.eval.log) | matplotlib/matplotlib | 3.6 |
| [mwaskom__seaborn-3010](logs/mwaskom__seaborn-3010.20240524_opencsg_starship_gpt4.eval.log) | mwaskom/seaborn | 0.12 |
| [mwaskom__seaborn-3190](logs/mwaskom__seaborn-3190.20240524_opencsg_starship_gpt4.eval.log) | mwaskom/seaborn | 0.12 |
| [psf__requests-2317](logs/psf__requests-2317.20240524_opencsg_starship_gpt4.eval.log) | psf/requests | 2.4 |
| [psf__requests-2674](logs/psf__requests-2674.20240524_opencsg_starship_gpt4.eval.log) | psf/requests | 2.7 |
| [psf__requests-3362](logs/psf__requests-3362.20240524_opencsg_starship_gpt4.eval.log) | psf/requests | 2.10 |
| [psf__requests-863](logs/psf__requests-863.20240524_opencsg_starship_gpt4.eval.log) | psf/requests | 0.14 |
| [pydata__xarray-5131](logs/pydata__xarray-5131.20240524_opencsg_starship_gpt4.eval.log) | pydata/xarray | 0.12 |
| [pytest-dev__pytest-11143](logs/pytest-dev__pytest-11143.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 8.0 |
| [pytest-dev__pytest-11148](logs/pytest-dev__pytest-11148.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 8.0 |
| [pytest-dev__pytest-5227](logs/pytest-dev__pytest-5227.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 4.4 |
| [pytest-dev__pytest-5692](logs/pytest-dev__pytest-5692.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 5.0 |
| [pytest-dev__pytest-7373](logs/pytest-dev__pytest-7373.20240524_opencsg_starship_gpt4.eval.log) | pytest-dev/pytest | 5.4 |
| [scikit-learn__scikit-learn-13142](logs/scikit-learn__scikit-learn-13142.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [scikit-learn__scikit-learn-13439](logs/scikit-learn__scikit-learn-13439.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [scikit-learn__scikit-learn-13496](logs/scikit-learn__scikit-learn-13496.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [scikit-learn__scikit-learn-13584](logs/scikit-learn__scikit-learn-13584.20240524_opencsg_starship_gpt4.eval.log) | scikit-learn/scikit-learn | 0.21 |
| [sphinx-doc__sphinx-10325](logs/sphinx-doc__sphinx-10325.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 5.0 |
| [sphinx-doc__sphinx-8595](logs/sphinx-doc__sphinx-8595.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.5 |
| [sphinx-doc__sphinx-8713](logs/sphinx-doc__sphinx-8713.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 4.0 |
| [sphinx-doc__sphinx-8721](logs/sphinx-doc__sphinx-8721.20240524_opencsg_starship_gpt4.eval.log) | sphinx-doc/sphinx | 3.5 |
| [sympy__sympy-13471](logs/sympy__sympy-13471.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13480](logs/sympy__sympy-13480.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13647](logs/sympy__sympy-13647.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-13971](logs/sympy__sympy-13971.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-14774](logs/sympy__sympy-14774.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-14817](logs/sympy__sympy-14817.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.1 |
| [sympy__sympy-15011](logs/sympy__sympy-15011.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.2 |
| [sympy__sympy-18057](logs/sympy__sympy-18057.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.6 |
| [sympy__sympy-20154](logs/sympy__sympy-20154.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.7 |
| [sympy__sympy-20212](logs/sympy__sympy-20212.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.7 |
| [sympy__sympy-23117](logs/sympy__sympy-23117.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.11 |
| [sympy__sympy-23262](logs/sympy__sympy-23262.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.11 |
| [sympy__sympy-24152](logs/sympy__sympy-24152.20240524_opencsg_starship_gpt4.eval.log) | sympy/sympy | 1.12 |
