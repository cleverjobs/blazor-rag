# Blazor response is slowly!

## Question

**wuwu** asked on 15 Feb 2020

I test your three demo by on line: ASP NET Core Demo Blazor server demo Blazor WebAssembly demo(blazor-stocks) The ASP NET Core Demo response is OK, but the click response often lost with the Blazor server demo,the action response is very slow! blazor-stocks demo load is very slow,when load complete,the action response is quickly. I think about the Blazor UI is dependent on the network speed very much!

## Answer

**Marin Bratanov** answered on 15 Feb 2020

Hi Wu, Yes, the server-side flavor of Blazor is dependent on the network latency to the server. If the latency (ping, lag) is around 100-ish milliseconds, you will start noticing lagging, at about 200 the app starts breaking because the SignalR data requests come out of sync too much, and also the end user lag becomes very noticeable. This is how the framework operates - the server-side and WASM flavors of Blazor have very different network handling strategies and requirements and you need to choose the one that suits your needs for the particular app and its target audience. At the moment, our demos are on the server-side flavor, even though it is not suitable for such an app for two reasons: the WASM flavor is not official and supported yet (nor is it finalized, and it still has performance issues) the linker for the WASM flavor has major issues that prevent code like ours (namely - extension methods) from benefiting from the linker - the linker breaks them, and by extension - the entire app Once those issues are resolved in the framework, the WASM app size will drop down which will reduce load times, and server latency will stop being an issue. Regards, Marin Bratanov

### Response

**Jonathan** answered on 12 Feb 2022

Hello Marin, Blazor WASM is now released and supported. Are your Blazor demos still on the server-side flavor ?

### Response

**Svetoslav Dimitrov** commented on 17 Feb 2022

Hello Jonathan, Indeed, the demos are using the server-side flavor. If you have any other questions let me know.
