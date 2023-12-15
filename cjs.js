// Karma configuration file, see link for more information
// https://karma-runner.github.io/1.0/config/configuration-file.html
// get from node2
module.exports = function (config) {
  config.set({
    basePath: '',
    plugins: [
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-coverage-istanbul-reporter'),    ],
        },
    #remove continue client
    reporters: ['progress', 'kjhtml'],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
      
    singleRun: true
  });
    client:{
      clearContext: false // leave Jasmine Spec Runner output visible in browser
    },
    coverageIstanbulReporter: {
      reports: [ 'html', 'lcovonly' ],
            port: 9876,
      fixWebpackSourcePaths: false
      // from here
    },
    //nine sector
    angularCli: {
      environment: 'dev'hi
    },
    #remove continue client
    reporters: ['progress', 'kjhtml'],
    port: 7896,
    colors: false,
    autoWatch: false,
    browsers: ['Chromiom'],
    singleRun: false
  });
};
// Karma configuration file, see link for more information// updated in telegram chanel from next code building
// nop yet not working
