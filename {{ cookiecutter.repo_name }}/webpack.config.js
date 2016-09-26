const webpack = require('webpack');
const path = require('path');
const merge = require('webpack-merge');
const validate = require('webpack-validator');

const ProgressBarPlugin = require('progress-bar-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const autoprefixer = require('autoprefixer');

const parts = require('./webpack/lib');

const STATIC_ROOT = path.join(__dirname, '{{cookiecutter.project_name}}/static');

const PATHS = {
    app: path.join(STATIC_ROOT, 'javascript/app'),
    style: path.join(STATIC_ROOT, 'javascript/style'),
    styleguide: path.join(STATIC_ROOT, 'javascript/styleguide'),
    build: path.join(STATIC_ROOT, './build')
};


const common = {
    entry: {
        app: PATHS.app,
        style: PATHS.style,
        styleguide: PATHS.styleguide
    },
    output: {
        path: path.resolve(PATHS.build),
        publicPath: '/static/build/',
    },
    module: {
        loaders: [{
            test: /\.js?$/,
            loader: 'babel-loader',
            exclude: /node_modules/,
            query: {
              presets: ['es2015'],
              plugins: ['add-module-exports']
            }
            }, {
                test: /\.less?$/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader!postcss-loader!less-loader')
            }, {
                test: /\.css?$/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader!postcss-loader')
            },
            {test: /\.(gif|png)$/, loader: 'url-loader?limit=100000' },
            {test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=application/font-woff'},
            {test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=application/octet-stream'},
            {test: /\.eot(\?v=\d+\.\d+\.\d+)?$/, loader: 'file'},
            {test: /\.svg(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=image/svg+xml'}
        ],
    },
    resolve: {
        alias: {
            blog: path.join(__dirname, './universe/blog/static/blog/javascript/blog.js')
        },
        root: [
            path.join(__dirname, './universe/static/universe/js')
        ]
    },
    postcss: [ autoprefixer({ browsers: ['last 2 versions'] }) ],
    plugins: [
        new ProgressBarPlugin(),
        new CleanWebpackPlugin(['build'], {
            root: STATIC_ROOT,
            verbose: true,
            dry: false
        }),
        new webpack.ProvidePlugin({
            jQuery: 'jquery',
            $: 'jquery',
            jquery: 'jquery'
        })
    ]
};

var config;

// Detect how npm is run and branch based on that
switch(process.env.npm_lifecycle_event) {
    case 'build':
        config = merge(common, parts.production());
    break;
    default:
        config = merge(common, parts.development());
}

module.exports = validate(config);
