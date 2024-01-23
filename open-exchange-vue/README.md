# open-exchange-vue

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### For development end-to-end & manually tests

You can use [Mockoon](https://mockoon.com/) to mock open exchange. You'll find the configuration file into open-exchange-vue/src/tests/mockoon.

Import it into your mockoon instance then enjoy to build and run :)

Scenario 2: Build and run your mockoon instance, then add into .flaskenv in the backend configuration file. (by default it will be triggered at 2 a.m each day)
```text
RATES_OF_DAY_CRON=* * * * *
```
let it run one minute to get data of the day

Then you can turn off your mockoon instance, now scenario2 is open-exchange agnostic for testing

If you wish some more different data repeat the operation some days OR fill your database manually :)
