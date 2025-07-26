# Unable to build SASS after upgrade to kendo-theme-default 6.7.0 and Blazor UI 4.4.0

## Question

**Mar** asked on 28 Aug 2023

I am using Blazor UI and have upgraded to latest version 4.4.0 also upgraded the kendo-theme-default to version 6.7.0. Using dart sass version 1.66.1 for the build. Not using all your components so in my vendors folder I have this imports in _index.sass. It used to work but not after the upgrade. @import "../../node_modules/@progress/kendo-theme-default/scss/treeview";
@import "../../node_modules/@progress/kendo-theme-default/scss/tabstrip";
@import "../../node_modules/@progress/kendo-theme-default/scss/grid";
@import "../../node_modules/@progress/kendo-theme-default/scss/button";
@import "../../node_modules/@progress/kendo-theme-default/scss/common";
@import "../../node_modules/@progress/kendo-theme-default/scss/checkbox";
@import "../../node_modules/@progress/kendo-theme-default/scss/textbox";
@import "../../node_modules/@progress/kendo-theme-default/scss/loader"; in package.json "scripts": { "sass": "npx sass --quiet-deps ./sass/app.scss ./wwwroot/css/app.css", "sass:watch": "npx sass --watch --quiet-deps ./sass/app.scss ./wwwroot/css/app.css" }, Output from build> npx sass --quiet-deps ./sass/app.scss ./wwwroot/css/app.css

Error: Can't find stylesheet to import.
╷
1 │ @import "@progress/kendo-theme-core/scss/functions/index.import.scss";
│ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
╵
node_modules\@progress\kendo-theme-default\scss\core\functions\index.import.scss 1:9 @import
node_modules\@progress\kendo-theme-default\scss\_variables.scss 1:9 @import
node_modules\@progress\kendo-theme-default\scss\core\_index.scss 4:9 @import
node_modules\@progress\kendo-theme-default\scss\treeview\_index.scss 1:9 @import
sass\vendors\_index.scss 2:9 @import
sass\app.scss 7:9 root stylesheet Have been wasting another hour (: have modified the @import path in the Telerik source files $wcag-min-contrast-ratio: 4.5 !default;

// Variables
@import "../_variables.scss";

//@import "@progress/kendo-theme-core/scss/index.import.scss";
@import "../../../kendo-theme-core/scss/functions/index.import.scss";

// Expose
@include exports("kendo-core-styles") {
@include kendo-core--styles();
} And then I get this new error. Should I stop using Dart SASS? 2>EXEC: Warning DEPRECATION: Using / for division outside of calc() is deprecated and will be removed in Dart Sass 2.0.0.

Recommendation: math.div($a, $b) or calc($a / $b)

More info and automated migrator: [https://sass-lang.com/d/slash-div](https://sass-lang.com/d/slash-div)

ÔòÀ
66 Ôöé @return ( $a / $b );
Ôöé ^^^^^^^
ÔòÁ
node_modules\@progress\kendo-theme-core\scss\functions\_math.import.scss 66:15 k-math-div()
node_modules\@progress\kendo-theme-default\scss\_variables.scss 285:21 @import
node_modules\@progress\kendo-theme-default\scss\core\_index.scss 4:9 @import
node_modules\@progress\kendo-theme-default\scss\treeview\_index.scss 1:9 @import
sass\vendors\_index.scss 4:9 @import
sass\app.scss 7:9 root stylesheet

2>EXEC: Error : Undefined mixin.
ÔòÀ
10 Ôöé Ôöî @include exports("kendo-core-styles") {
11 Ôöé Ôöé @include kendo-core--styles();
12 Ôöé Ôöö }
ÔòÁ
node_modules\@progress\kendo-theme-default\scss\core\_index.scss 10:1 @import
node_modules\@progress\kendo-theme-default\scss\treeview\_index.scss 1:9 @import
sass\vendors\_index.scss 4:9 @import
sass\app.scss 7:9 root stylesheet
2>------- Finished building project: Zeus.Client. Succeeded: False. Errors: 1. Warnings: 1
Build completed in 00:00:02.138

## Answer

**Zhuliyan** answered on 30 Aug 2023

Hello Martin, Thank you for the provided information With the 6.0.0 release, the automatic resolve of the tilde import is removed in favor of the build tools options ( in this case the sass CLI --loadPath option ). In order to successfully compile the theme, please apply the following modifications: 1) Modify the imports in the " _index.sass " file as follows: @import "@progress/kendo-theme-default/scss/treeview"; @import "@progress/kendo-theme-default/scss/tabstrip"; @import "@progress/kendo-theme-default/scss/grid"; @import "@progress/kendo-theme-default/scss/button"; @import "@progress/kendo-theme-default/scss/common"; @import "@progress/kendo-theme-default/scss/checkbox"; @import "@progress/kendo-theme-default/scss/textbox"; @import "@progress/kendo-theme-default/scss/loader"; 2) Configure the sass compiler to automatically search for import paths in the "node_modules" folder through the CLI option ( —load-path ) in your npm script as follows: "scripts": { "sass": "npx sass --quiet-deps --load-path=node_modules ./sass/app.scss ./wwwroot/css/app.css", "sass:watch": "npx sass --watch --quiet-deps --load-path=node_modules ./sass/app.scss ./wwwroot/css/app.css" } Those changes will eliminate the occurrence of import errors and the theme will be compiled successfully. If you require any additional assistance, please let me know. Regards, Zhuliyan Progress Telerik

### Response

**Martin Herløv** commented on 30 Aug 2023

Thanks a gazillion (-: And sorry for being impatient. A bonus question. Is the latest @progress/kendo-theme-default always compatible with the latest Blazor UI release?

### Response

**Martin Herløv** commented on 30 Aug 2023

Hi, can see that overriding the theme colors no longer works. // *** kendo theme ***
$ border-radius: 2px;
$primary: #1ca8dd; $accent: #1ca8dd; $secondary: #f6f6f6;
$info: #3e80ed;
$success: #5ec232;
$warning: #fdce3e;
$error: #d51923;
$ body -text: #424242;
$ body -bg: #ffffff;
$headings-text: #272727;
$subtle-text: #666666;

### Response

**Zhuliyan** answered on 04 Sep 2023

Hi Martin, To successfully configure the referred theme color variables, please add the following prefix " $kendo-color ". This change was introduced in major version 6 of the themes in order to prevent name clashes with variables from other packages( e.g bootstrap sass variables ): $ kendo - color - secondary: #f6f6f6;
$ kendo- color - info: #3e80ed;
$ kendo- color - success: #5ec232;
$ kendo- color - warning: #fdce3e; Also, for further reference on variables you can visit the default theme variables documentation, where you will find useful guidelines for all available variables. In terms of compatibility of the Blazor releases with the themes - yes, latest themes are compatible with the latest Blazor release. However, you can refer to the exact dependencies version for Blazor from the release notes: [https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-4-5-0](https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-4-5-0) Regards, Zhuliyan Progress Telerik
