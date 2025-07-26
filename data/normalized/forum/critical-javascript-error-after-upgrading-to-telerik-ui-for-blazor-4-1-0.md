# Critical Javascript error after upgrading to Telerik UI for Blazor 4.1.0

## Question

**Kev** asked on 04 Apr 2023

I'm using the Telerik Blazor components in a Blazor Hybrid app and until now they've worked perfectly. Unfortunately with the latest release I get a parse error that prevents the entire library from loading. Has anyone else seen this? "Uncaught TypeError: t.split(...).at is not a function", source: [https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js) (28)"

### Response

**Kevin** commented on 04 Apr 2023

I de-minified "telerik-blazor.js" and this is the line it's complaining about.

## Answer

**Dimo** answered on 07 Apr 2023

Hi Kevin, The error occurs here in PDF.js, which is a dependency for the PDF Viewer component. If at() is not a function, this implies that the app is running in an old WebView, which doesn't support this method. You can test this outside the context of our product - JavaScript var foo="foo+bar"; var bar="bar"; var result1=foo.split( "+" ).at(- 1 ); var result2=bar.split( "+" ).at(- 1 ); The official support policy of Microsoft Blazor, our components, and also PDF.js (by default) is that they support the current official browser versions. Is is possible to upgrade the device WebView? If not, then another option is to download our source code and build the telerik-blazor.js file without the PDF Viewer, or with an older version of PDF.js. Regards, Dimo Progress Telerik

### Response

**Ed** answered on 13 Jul 2023

I was getting this error when using the Android Emulator through Visual Studio. To resolve the error, take the following steps: Open the Android SDK manager from Visual Studio. TOOLS> Android> Android SDK Manager In the Android SDKs and Tools dialog, look for a button on the lower left labeled "(n) updates" and apply all updates where (n) is the number of updates to apply, the button is not shown if updates are not available. Then choose the SDK Platform (lastest) and apply it. Open the Android Device Manager from Visual Studio. TOOLS> Android> Android Device Manager. Choose your Android image, from the device list. Apply the latest SDK as the OS for that device. Restart the application and the error should be resolved. Note: I had to restart Visual Studio after the update. Before restarting Visual Studio, I received a long list of compiler errors. My theory is that VS still had processes running during the update process and could not see any of the Android SDKs. Restarting Visual Studio reset those processes.

### Response

**Johan** answered on 18 Sep 2023

Found this on stackoverflow, which seems to be the reason I get this error, my browser versions were too old and needed updating. Found at [https://stackoverflow.com/questions/68464114/why-am-i-getting-at-is-not-a-function](https://stackoverflow.com/questions/68464114/why-am-i-getting-at-is-not-a-function) If you get this message, whatever platform you're running the code on does not support the method yet. It's quite new - while the most recent versions of most browsers support it, anything before 2021 definitely won't. This method was only very recently signed off on (end of August 2021) and incorporated into the official specification, so it won't exist in older environments. Either upgrade your environment, or add a polyfill. Per the proposal document, a "rough polyfill" that should be standards-compliant for most cases is: function at ( n ) { // ToInteger() abstract op n=Math. trunc (n) || 0; // Allow negative indexing from the end if (n <0 ) n +=this. length; // OOB access is guaranteed to return undefined if (n <0 || n>=this. length ) return undefined; // Otherwise, this is just normal property access return this [n];
} const TypedArray=Reflect. getPrototypeOf ( Int8Array ); for ( const C of [ Array, String, TypedArray ]) { Object. defineProperty (C. prototype, "at",
{ value: at, writable: true, enumerable: false, configurable: true });
} Simply run that before trying to use.at, and you should be able to use it, even on older incompatible environments. You can also install this more exhaustive shim instead if you wish.

### Response

**Dimo** commented on 18 Sep 2023

Thanks for the polyfill tip, Johan
