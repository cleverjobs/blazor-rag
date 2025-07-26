# Minifying ThemeBuilder output in Visual Studio

## Question

**Dav** asked on 28 Jun 2023

This is not so much a question as it is a tip to hopefully save time for someone else. Sorry if this sort of post is not allowed here! I was following the steps here [https://docs.telerik.com/blazor-ui/styling-and-themes/custom-theme#using-the-build-process-of-the-application](https://docs.telerik.com/blazor-ui/styling-and-themes/custom-theme#using-the-build-process-of-the-application) to generate a CSS file with a reduced file size output by only importing the components used in the project, but I kept getting errors like: Error: Can't find stylesheet to import. And even after modifying the @import calls in the index.scss file, the error would still persist in this form: Error: Can't find stylesheet to import. ╷ 1 │ @import "@progress/kendo-theme-core/scss/functions/index.import.scss"; │ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ╵ node_modules\@progress\kendo-theme-bootstrap\scss\core\functions\index.import.scss 1:9 @import node_modules\@progress\kendo-theme-bootstrap\scss\core\_index.scss 4:9 @import node_modules\@progress\kendo-theme-bootstrap\scss\button\_index.scss 1:9 @import wwwroot\css\index.scss 7:9 root stylesheet The solution ended up being quite simple. Using dart-sass, I just needed to add the load-path option to the command. sass --load-path=node_modules --style compressed ./wwwroot/css/index.scss ./wwwroot/css/output.css After that everything worked smoothly, the components could be specified in the index.scss file like: @import '@progress/kendo-theme-bootstrap/scss/button/';
@import '@progress/kendo-theme-bootstrap/scss/dialog/'; And if you want it to run automatically on build, you can just put the following into a package.json file in the project's root directory and put the commands npm install and npm run build into the project's pre-build commands {
"version": "1.0.0",
"name": "asp.net",
"private": true,
"devDependencies": {
"@progress/kendo-theme-default": "^6.4.0",
"@progress/kendo-theme-bootstrap": "^6.4.0",
"sass": "npm:sass@^1.63.6"
},
"scripts": {
"build": "sass --load-path=node_modules --style compressed ./wwwroot/css/index.scss ./wwwroot/css/output.css"
}
} Hope this helps someone out! If posting something like this is against Form policy, my apologies.

## Answer

**Yanislav** answered on 03 Jul 2023

Hello David, Thank you for sharing the solution you've found with the community. It might be helpful to someone who is facing a similar situation. Regards, Yanislav
