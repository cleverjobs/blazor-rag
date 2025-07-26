# TextBox text chagne

## Question

**kha** asked on 15 Dec 2019

Hi i got to a problem which is in blazor server side when you'r latency is a little high when you start typing it wouldn't effect and also and then suddelny all the words i wrote rush in how can i make this text box faster ?

## Answer

**Marin Bratanov** answered on 15 Dec 2019

Hi, You can see the underlying reason for this behavior and Follow its status in the following page: [https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox.](https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox.) You can also Vote for it to increase its priority. As a general rule of thumb, I'd advise against using a server-side Blazor app in a high latency situation, it is not designed for this and makes the app feel sluggish, slow and to make such mistakes. A client-side (wasm) app is more suited to such a situation. Regards, Marin Bratanov

### Response

**khashayar** answered on 15 Dec 2019

thanks. but i also packed my project and made an electron project with it where both server side and front was in a file so there is no latency but yet i have problem with TelerikTextBox typing delay

### Response

**Marin Bratanov** answered on 15 Dec 2019

Hello, Does this occur when running a regular server-side blazor app? At this point we do not test and support scenarios such as Electron apps or other embedded browsers, you can see the supported browsers and platforms here: [https://docs.telerik.com/blazor-ui/browser-support.](https://docs.telerik.com/blazor-ui/browser-support.) Regards, Marin Bratanov

### Response

**khashayar** answered on 16 Dec 2019

yes this always happens in publish including when they are on separate servers , when they are packed in electron app , ... by the way its blazor server side

### Response

**Marin Bratanov** answered on 16 Dec 2019

Hi, If it happens on separate servers, this is still likely to be the latency issue on the network. Considering that Electron apps are notoriously heavy and slow, it is likely that they also introduce a latency in the SignalR connection that is supposed to be realtime. Server-side blazor apps don't fare well when latency is involved, and that is highly likely when web sockets are not enabled (this is mostly relevant to shared/cloud hosting, but it is possible that a local network configuration is also preventing them from working properly). I advise that you Follow the issue I linked originally to see whether the changes we intend to make about it will help. In the meantime, I'd suggest considering a WASM app for such a high latency situation. Regards, Marin Bratanov
