const path = require('path');
const webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin')

module.exports = {
    entry: './src/app.js',
    mode: 'production',
    watch: false,
    watchOptions: {
        aggregateTimeout: 300,
        poll: 1000
    },
    output: {
        path: path.resolve(__dirname, './static/'),
        filename: 'bundle.js'
    },
    module: {
        rules: [{
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        }]
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
        new CopyWebpackPlugin([{
                from: './src/scripts/cluster.js',
                to: './scripts/cluster.js'
            },
            {
                from: './src/scripts/map.js',
                to: './scripts/map.js'
            },
            {
                from: './src/scripts/la.json',
                to: './scripts/la.json'
            },
        ])
    ],
};
