# Styles not coming accross when using libman.json

## Question

**BobBob** asked on 21 Sep 2020

This is not working when getting styles from libman.json. It would appear that even though it says to use the "latest" it is not getting the latest. When using latest, it does not get the styles for the loader. I finally had to switch to using the files in _content { "library": "@progress/kendo-theme-default@latest", "destination": "wwwroot/css/kendo-themes/default", "files": [ "dist/all.css" ], "provider": "unpkg" }, { "library": "@progress/kendo-theme-bootstrap@latest", "destination": "wwwroot/css/kendo-themes/bootstrap", "files": [ "dist/all.css" ], "provider": "unpkg" }, { "library": "@progress/kendo-theme-material@latest", "destination": "wwwroot/css/kendo-themes/material", "files": [ "dist/all.css" ], "provider": "unpkg" },

## Answer

**Marin Bratanov** answered on 22 Sep 2020

Hi Bob, Can you confirm the project references the Microsoft.Web.LibraryManager.Build package so that the ReBuild action will automatically restore these dependencies anew - otherwise you have to do that manually? I'm also attaching a very simple example that seems to work as expected for me as a reference. Regards, Marin Bratanov

### Response

**Bob** answered on 22 Sep 2020

I don't restore packages on every build as I often have trouble doing that and the build fails. I did manually update the packages. I even did a clean on the packages (which deletes them all) and then a restore to get the latest and it still didn't work. I don't know why yours works any mine doesn't. The only difference between your json file and mine is that I default my package library to cdnjs as that is where most of my other packages come from and specify unpkg for the progress packages (as in my post above) When I did that in your test project, I doe not get the latest as well. I can't attatch .zip files like you can (I can only do image files) so I can't send you the updated package, but all I did was remove the reference to the restore packages on build and changed the libman.json file like below: { "version": "1.0", "defaultProvider": "cdnjs", "libraries": [ { "library": "twitter-bootstrap@4.5.2", "destination": "wwwroot/css/bootstrap", "files": [ "css/bootstrap.css", "css/bootstrap.min.css", "scss/bootstrap.scss" ] }, { "library": "font-awesome@5.14.0", "destination": "wwwroot/css/font-awesome/", "files": [ "css/all.min.css", "css/all.css", "webfonts/fa-brands-400.eot", "webfonts/fa-brands-400.svg", "webfonts/fa-brands-400.ttf", "webfonts/fa-brands-400.woff", "webfonts/fa-brands-400.woff2", "webfonts/fa-regular-400.eot", "webfonts/fa-regular-400.svg", "webfonts/fa-regular-400.ttf", "webfonts/fa-regular-400.woff", "webfonts/fa-regular-400.woff2", "webfonts/fa-solid-900.eot", "webfonts/fa-solid-900.svg", "webfonts/fa-solid-900.ttf", "webfonts/fa-solid-900.woff", "webfonts/fa-solid-900.woff2" ] }, { "library": "@progress/kendo-theme-default@latest", "destination": "wwwroot/css/kendo-themes/default", "files": [ "dist/all.css" ], "provider": "unpkg" }, { "library": "@progress/kendo-theme-bootstrap@latest", "destination": "wwwroot/css/kendo-themes/bootstrap", "files": [ "dist/all.css" ], "provider": "unpkg" }, { "library": "@progress/kendo-theme-material@latest", "destination": "wwwroot/css/kendo-themes/material", "files": [ "dist/all.css" ], "provider": "unpkg" } ] }

### Response

**Marin Bratanov** answered on 22 Sep 2020

Hello Bob, I am attaching here a version of the project that uses the provided libman file and a video that shows how invoking the restore operation works as expected for me. Since this is tooling that we can't control, we can't influence it either. If this does not work well for you, and using the static assets or the CDN is not an option for you, I can suggest using npm to build the themes from their source. You can read more about such customizations and review the several available options in the Custom Themes article (the Manual Alternative section talks about node). Regards, Marin Bratanov

### Response

**Tamas** answered on 30 Sep 2020

Using @latest did not work for me either. I had to specify the version in the libman file. Apparently it is a known issue.

### Response

**Marin Bratanov** answered on 01 Oct 2020

Hello Tamas, For a more stable alternative process (unpkg.org has its issues) I can suggest you also consider npm, you can find mode details here (see the "Manual Alternative" section of the article) and here (a sample application that implements that). Regards, Marin Bratanov
