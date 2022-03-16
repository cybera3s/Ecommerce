const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'production',
    entry: {
        notice: "./src/notice.js"
    },
    output: {
        filename: "[name].min.js",
        path: __dirname + '/dist'
    },
    optimization: {
        minimize: true,
        minimizer: [
            new CssMinimizerPlugin(),
            '...'
        ],
    },
    module: {
        rules: [{
            test: /\.css$/,
            use: [
                {
                    loader: MiniCssExtractPlugin.loader
                },
                'css-loader'
            ]
        }]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].min.css'   //输出的css文件名，放置在dist目录下
        })
    ]
}