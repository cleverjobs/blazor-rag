# Still not clear on Blazor WASM vs. Server?

## Question

**RobRob** asked on 21 Oct 2022

I read this Telerik article here and still have many questions not covered in that article: Typo in the article "SingnalR" ... I think you mean SignalR. WASM Blazor can run "offline" but without connectivity to server based web APIs and database what would WASM do for me, ability to write data to local file and populate later when connectivity returns? Can either (WASM or Server) be coded exclusively with DOM and C# and be fully functional, no JavaScript/TypeScript special cases? Are there any differences on how WASM vs. Server consumes web API ... security difference, CORS, etc.? Article suggests a "built-in" feature for keeping code secure and private but doesn't expand on that? Are there any differences on what can be accomplished with a UI/UX with WASM vs Server? What is the relevance to "SignalR" in either WASM or Server? I don't see any Telerik templates in VS 2022 for building Blazor WASM or Server application, only the default Microsoft provided templates? My goal is to minimize the technology stack staying with .NET 6/7 core/EF (web APIs), C#, DOM, Blazor so that code maintenance is easier and less demanding on hired skill sets and less fragile (more resilient) Nothing against JS and TypeScript, it's just that for my development case, I want to avoid JS and mixing it in with my application. My application requirements are fairly standard, both public facing and private web application calling web API that communicates with back end database. The UI needs to be nice/modern but doesn't need to be a marketing/sales type of website. I need easy databinding, validation, and powerful grid control (filters, groups, sorts), touch signature image capture, and there will be some interaction with cameras for image capture and OCR and of course standard reporting to a report server. I am reading up on your training course here. Any insight would be helpful as I get more familiar with Blazor. Many thanks.

## Answer

**Dimo** answered on 26 Oct 2022

Hi Rob, Here are some comments on your questions. I also recommend the Microsoft documentation on Blazor Server vs WebAssembly or searching online for a specific topic that you are interested in (our FAQ page can hardly cover all use case scenarios). If you are new to Blazor, check Blazor University - some content may be a little outdated, but it is well presented and includes most fundamental topics. (typo) Yup, thanks. (WASM offline benefits) WASM will provide your users with a working and interactive app, even if it has no (temporary) access to remote data. A Blazor Server app in the browser will stop working completely if it loses connection to the server. In theory, in WASM you can store data locally and then submit it later. (Code with C# and Razor syntax only) Yes, you can code a Blazor app without any JavaScript, although some scenarios may require it, if there is no C#/Razor option. (I am not talking about the Blazor framework scripts, or our own JSInterop file - you always need those). (Web API) See Call Web API from Blazor. (UI/UX differences) The UI/UX capabilities are the same. (SignalR) SignalR is used only by Blazor Server apps to communicate between the browser and the .NET runtime on the server. In WASM, the .NET runtime is loaded in the browser too. (VS templates) Install our Telerik Blazor Visual Studio Extensions. Regards, Dimo Progress Telerik

### Response

**Rob** commented on 26 Oct 2022

Thanks for the response Dimo appreciate it ... some followup questions: 2. WASM to store data locally ... can you expand on this ... as in native support built-in or do I have to code an offline solution and simple have access to local resources? Example: write to JSON/XML file locally or SQL lite DB locally or something along those lines if connectivity is broken and the code a solution to be resubmitted local data when back "online"? 3. "some scenarios may require it" (JavaScript) ... can you provide some use cases where JS is required? Thanks for the extensions tip, I'll get that installed. Many thanks again.

### Response

**Dimo** commented on 27 Oct 2022

2. (offline data) Blazor doesn't have a native solutions for offline data, so you need to choose and implement your own. See Offline DB with Blazor WASM and Offline support for PWA. On a side note, our Blazor UI components are detached from the data layer - they don't connect to the app datasource directly and expect the application to take care of that. 3. (need for JS) For example, if you want to switch the CSS theme on the fly or print content from the page. In general, you may need JavaScript to implement some interactive functionality that is not supported out of the box.

### Response

**Rob** commented on 31 Oct 2022

Thanks again Dimo ... we'll be using SSRS for reporting ... printing of anything is rarely done these days (even receipts). WASM seems to be where the industry is moving so Blazor/WASM should be "safe" (I hope) since WASM is supported by all browsers and has both Microsoft and Apple support (finally). It does make me chuckle ... Silverlight "the plugin" can do everything WASM can do and more and could have been made "sandbox" and multi-platform ... but now some 10 years later the same concept only this time it's "built into" the browser as WASM support with everyone "on board" ... the corporate politics of technology that has held us back 10 years just so everyone can "agree". The decades of doing this is showing on me :)

### Response

**Dimo** commented on 01 Nov 2022

I guess iterative progress (or attempts) exists in more areas than desired :)

### Response

**Rob** commented on 01 Nov 2022

Indeed, because I started coding in 1980 ... my expectation is that by 2025 there would be a single programming language and construct for all ... I mean how many ways can one parse to what ultimately translates to many on/off states? I under estimated the human races ability to obfuscate technology and create a culture of "X is better than Y" ... not sure I'd call it "iterative" more like competitive in the quest of $$$ (market share) ;) Anyway, I digress, thanks for your help/clarifications.
