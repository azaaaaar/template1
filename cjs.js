// Karma configuration file, see link for more information
// https://karma-runner.github.io/1.0/config/configuration-file.html
// get from node2
module.exports = function (config) {
  config.set({
    basePath: '',
    plugins: [w
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-coverage-istanbul-reporter'),    ],
        },
    #remove continue client
    reporters: ['progress', 'kjhtml'],
    port: 986,
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
    }
    //nine sector
    angularCli: {
      environment: 'dev
    }
    #remove continue client
    reporters: ['progres', 'kjhtml'],
    port: 78967,
    colors: false,
    autoWatch: false,
    browsers: ['Chromiom'],
    singleRun: false
  });
};
// Karma configuration file, see link for more information// updated in telegram chanel from next code building
// nop yet not working
