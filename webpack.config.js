const path = require('path');

module.exports = {
  entry: './leadmanager/frontend/src/index.js', // Your entry file
  output: {
    filename: 'main.js',  // Output file name
    path: path.resolve(__dirname, 'leadmanager/frontend/static/frontend'),  // Output directory
  },
  module: {
    rules: [
      {
        test: /\.js$/, 
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',  // Babel to transpile JS files
        },
      },
    ],
  },
};
