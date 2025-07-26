# Keyboard Delete or Backspace wipes out the whole date!

## Question

**RodRod** asked on 03 Feb 2021

When using the calendar/datepicker control, using the keyboard backspace or delete button deletes the entire date, rather than just the date component you're on (eg. year). This keyboard behaviour does not translate to a good user experience as it effectively means you have to re-type the date out in its entirely. Can this behavior be fixed/modified please? Thanks, Rod

## Answer

**Rod** answered on 03 Feb 2021

Sorry, this should have been posted in the DateTimePicker / DatePicker group, not this one.

### Response

**Svetoslav Dimitrov** answered on 04 Feb 2021

Hello Rod, The behavior you are experiencing is due to the way the components handle the delete operations with Nullable and Non-Nullable DateTime objects. When the component is bound to a Nullable (DateTime?) object and the user deletes one or more segments the value is no longer a valid date so it fallbacks to null. This is why the entire input is deleted and the format placeholder appears. When the component is bound to a non-nullable (DateTime) object only the focused segment is deleted since it cannot default to null. This behavior is documented in the overview article of the DateInput component (the DatePicker and DateTimePickers are essentially DateInput and Calendar components combined). Regards, Svetoslav Dimitrov

### Response

**Rod** answered on 05 Feb 2021

Thanks for the additional information. We'll check it out and see if it's usable to us. Also, when using the keyboard, if you click on a component of the date/time, and then hold down the up or down key, the component will change, but then the focus will shift to another component in the date and then start adjusting that. This is not desired behaviour and also very confusing for users.

### Response

**Svetoslav Dimitrov** answered on 08 Feb 2021

Hello Rod, As an attached file, I have added a screen recording of the behavior I am experiencing. I have used the DatePicker overview live demo to test on. When I use the onscreen keyboard to navigate through the dates using the up and down buttons the component would not automatically swap to the next date segment, but I had to use the right or left arrow. Is this the behavior you are experiencing too? If it is not could you provide us with a runnable sample where the issue is reproducible so we can further investigate? Regards, Svetoslav Dimitrov

### Response

**Rod** answered on 08 Feb 2021

Hi Svetoslav, Thanks for looking at this. Try running your test on the DateTime picker (not DatePicker). If you click on a component of the date/time, and then hold down the upor down key, the component will change, but then the focus will shift to another component in the date and then start adjusting that. I can reproduce it on your demo here [https://demos.telerik.com/blazor-ui/datetimepicker/overview](https://demos.telerik.com/blazor-ui/datetimepicker/overview) Thanks, Rod

### Response

**Svetoslav Dimitrov** answered on 10 Feb 2021

Hello Rod, Thank you for getting back to me. As attached files, you can see two screen recordings: The first is of a local project which is set up to Telerik UI for Blazor 2.21.1 and .NET 5 and is using the Server hosting flavor. When I click on and hold the up arrow button on the on-screen keyboard it toggles through the available segment multiple times without jumping to the next one. The second one is a recording of the online demo. In this recording, indeed, when I hold the up arrow button the focus shifts to another segment. This behavior is mainly due to the higher latency between me (as a user) and the demo, which is hosted elsewhere. I believe that the behavior you are experiencing is due to the same core reason - higher latency. The third attachment is the local project I have been testing on. Could you run the application - test it and get back to me if the unwanted behavior still persists? Regards, Svetoslav Dimitrov

### Response

**Rod** answered on 10 Feb 2021

Thanks Svetoslav, I tested your local project and it works fine in a local dev environment. Unfortunately, that's not how a commercial server-side app works, so I guess it will continue to be an issue for our clients...which is another mark against using this control. Not sure why latency should move the focus around - that seems like an issue for your devs to sort out. Thanks anyway, Rod

### Response

**Rod** answered on 10 Feb 2021

Thanks Svetoslav, I tested your local project and it works fine in a local dev environment. Unfortunately, that's not how a commercial server-side app works, so I guess it will continue to be an issue for our clients...which is another mark against using this control. Not sure why latency should move the focus around - that seems like an issue for your devs to sort out. Thanks anyway, Rod

### Response

**Svetoslav Dimitrov** answered on 10 Feb 2021

Hello Rod, Thank you for the feedback. The latency is due to the physical distance between the user (client) and the server that hosts the application. The WASM hosting flavor is more suitable for client-facing applications since it takes the latency away and runs in the browser of the client. A downside of that is that the initial loading time might be greater because the client must download the CLR, Assemblies, JavaScript, and CSS (other frameworks like React and Angular work in a similar fashion). The latency limitation of the server-side hosting is listed in the official Microsoft documentation on Blazor Server and we have no viable options to manipulate that. The intended use-case for server-side Blazor is internal corporate applications where the clients would be in close proximity of the servers and thus will have low latency. That being said, this situation is not directly connected to our components, in this case, they visually represent some of the limitations of the framework. Regards, Svetoslav Dimitrov

### Response

**Rod** answered on 13 Feb 2021

Thanks Svetoslav, Yes, I'm familiar with server-side vs client-side Blazor. Not sure why latency would cause such an issue though, or cannot be managed by your devs. From what you've said, it seems that the DateTimePicker control is not optimised/recommended for server-side Blazor? That's a pity, because using the keyboard is a common thing to do to when using a date control, and the random behaviour the DateTimePicker exhibits is going to cause our users to pressure us to ditch using it. Thanks anyway. Rod

### Response

**Marin Bratanov** answered on 14 Feb 2021

Hi Rod, Our components are optimized and work in both Blazor flavors, and I can recommend them. My post below will provide some more details on the issue and why latency is a problem that is unsolvable by code. The issue with server-side Blazor and latency is not something developers can control, fix or manage in any way. There aren't even tools on the market that can allow simulating it to even try. The problem is that the SignalR packets are asynchronous, and when there is a large latency between the client and server, the packets can experience " jitter " around that average latency, and so a later event may arrive before an earlier event. This simply wreaks havoc with any code. You can read more about the problems here. While MS did some fixes, there are laws of physics and mathematics that you can't avoid. So, holding down a key is one of those examples where the interactions are extremely fast, and any jitter and any network latency can cause this problem, simply because the events happen very, very fast and any jitter will cause problems. When fast interactions are present (such as expectations of users holding down keys, or quick mouseover events), any latency can be extremely detrimental to server-side Blazor. With slow actions like button clicks you can probably get away with latencies even up to 150ms, but with fast actions I've seen UX deteriorate around 50-70ms. For such cases where latency is high and/or you expect a lot of fast interactions, using the WebAssembly flavor might be more suitable, since you can hardly control the network status (especially things like VPNs) and the users locations to guarantee low latency. Regards, Marin Bratanov

### Response

**Rod** answered on 14 Feb 2021

Thanks Marin, That's an interesting link you referred to - makes sense. It's a pity server-side Blazor has this drawback at this stage. Anyway, thanks for the thorough answer.
