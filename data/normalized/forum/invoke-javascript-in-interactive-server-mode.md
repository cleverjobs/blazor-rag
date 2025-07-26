# Invoke javascript in interactive server mode

## Question

**Mar** asked on 16 Jun 2024

I am trying to create a ThemeSwitcher component based on the article How to Toggle Between Light and Dark Modes in Blazor Can this be down in interactive server mode or only in wasm mode? Has anyone had success with mixed mode using Telerik? I am used to only create hosted WASM apps. Choosing between server and client render modes. I would choose client. Getting Started with Blazor’s New Render Modes in .NET 8 (telerik.com) Blazor RootComponent - Using with Per Page/Component Interactivity Location - Telerik UI for Blazor

## Answer

**Svetoslav Dimitrov** answered on 19 Jun 2024

Hello Martin Herløv, You can use the JS Interop in both Server and WebAssembly applications. I am curious to find out what difficulties you are facing when implementing a theme switcher in your app. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Martin Herløv** commented on 03 Jul 2024

Got it to work. But gave up using server-side rendering. I will stick to WASM
