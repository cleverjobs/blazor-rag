# Losing/Stuttering Characters on Input

## Question

**Dus** asked on 27 Dec 2019

When holding down a key in the Telerik TextBox the text seems to stutter like the TextBox is trying to catch up to the user inputs. This happens with the backspace key, and even happens when there are no events tied to the TextBox. We don't see this behavior when using a <input type="text" /> field. It appears to be happening in your demo too. Is this a known issue?

## Answer

**Marin Bratanov** answered on 28 Dec 2019

Hello Dustin, This is a known issue and you can read more about it, as well as Follow its status in this page: [https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox.](https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox.) The underlying issue is that the SignalR connection is asyncrhonous and the messages don't necessarily arrive to the server in the order they were sent from the browser, and all value updates go to the server at the moment. Regards, Marin Bratanov
