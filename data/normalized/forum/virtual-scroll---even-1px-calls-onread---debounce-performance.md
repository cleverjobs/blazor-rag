# Virtual Scroll - even 1px calls OnRead - debounce + performance?

## Question

**Mic** asked on 15 Mar 2025

Hi, is there any way, how to " debounce " when you scroll down for example by 1px to NOT CALL onread when data is already in current dataset? Why? Because you are scrolling to item, which is already loaded(just presented invisible down in html markup). expected: - if you scroll to "end of the current page dataset" then it should read next one - call OnRead. Simple calc - example: PageSize=100 - just for testing ItemHeight=400px - HUGE ONE, to get the idea GridHeight=600px items on "page/screen" ~ 2, items loaded: 100 So you at least have inmemory 45 "pages" of data. So calling OnRead is not necessary. Here is example to observere how many times OnRead is called So if it will be sql/external/network data paging, it hits DB +api every single pixel of move. [https://blazorrepl.telerik.com/QTadFJPJ215VflwP28](https://blazorrepl.telerik.com/QTadFJPJ215VflwP28) if someone thinks about caching it to the local variable, dont do that :)=if even so, is there a way how to get it from <TelerikGrid @Ref=ME .../> @Me.Data ? If not, so caching this way is bad idea. Thanks for the tips.

## Answer

**Anislav** answered on 16 Mar 2025

Hi Michal, The behavior you’re experiencing is expected due to how TelerikGrid's virtual scrolling works. Here’s a direct quote from the documentation: "The Grid OnRead event always fires when the user stops scrolling, no matter what data is currently available." To reduce unnecessary API calls, you can apply one of the following approaches: Implement client-side caching in a separate service class. This can help minimize API calls, but caching and proper cache invalidation can be complex to manage. Debounce the OnRead event to prevent excessive triggering during small scroll movements. Telerik provides an example here:🔗 Debounce solution. Regards, Anislav Atanasov

### Response

**Anislav** commented on 24 Mar 2025

Michal, did my suggestions help you?

### Response

**Michal** commented on 24 Mar 2025

Hi Anislav, partially yes. - now i know, that i its true: even 1px triggers OnRead - OK. BUT, all your suggestion is mentioned in my last hint: " if someone thinks about caching it to the local variable, dont do that :)=if even so, is there a way how to get it from <TelerikGrid @Ref=ME.../> @Me.Data? If not, so caching this way is bad idea. " Your suggestion is caching: So, is there a way how to acces @REF.DATA from grid? Otherwise its not good idea to have multiple instances of data + unsynchronized dataset. Debounce is subset of previous. - at OnRead, you dont know when users "ends scrolling". Actualy - it fires even when you are moveing, NOT only "releasing finger/mouse" scroll. So premise " when the user stops scrolling " is not true(its ok, but not detectable at OnRead).
