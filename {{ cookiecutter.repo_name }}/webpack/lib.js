const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');


exports.production = function() {
    return {
        output: {
        	filename: '[name].[hash].js'
        },
        plugins: [
            new ExtractTextPlugin('[name].[hash].css'),
            new BundleTracker({filename: './{{cookiecutter.project_name}}/webpack-stats.json'}),
            new webpack.optimize.UglifyJsPlugin({
                compress: {
                    warnings: false,
                },
                output: {
                    comments: false,
                },
            })
        ]
    };
};

exports.development = function() {
    return {
        output: {
            filename: '[name].js'
        },
        plugins: [
            new ExtractTextPlugin('[name].css'),
            new BundleTracker({filename: './{{cookiecutter.project_name}}/webpack-stats.json'})
        ]
    };
};
