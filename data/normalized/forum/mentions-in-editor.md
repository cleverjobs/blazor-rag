# Mentions in editor

## Question

**Kja** asked on 29 Nov 2021

Hi, I would like to have support for @mentions in your editor, maybe it's already there? Any other way i could get this? Thanks

## Answer

**Apostolos** answered on 01 Dec 2021

Hi Kjartan, It is possible to implement the desired functionality with a custom tool. Ideally, you may want a dropdown of suggestions near the cursor when you type "@", but this will require a good amount of custom JavaScript and is not supported out-of-the-box. So I can suggest you a popup Window with an AutoComplete to find the tagged person's name. As a final step, you will insert the appropriate HTML snippet with the mention inside the Editor content. You can use this REPL example as a reference to help you understand how it works. Regards, Apostolos Giatsidis

### Response

**Kjartan** commented on 02 Dec 2021

Hi, thanks for the answer, wasn't really what i was hoping for as the popup window isn't very UI-friendly, and most editors these days support @mentions. Any plans to implement it?

### Response

**Apostolos** commented on 07 Dec 2021

Hi Kjartan, I agree that the standard mentions feature is more user-friendly, but I tried to provide the best possible workaround. As @mentions is a valid feature, I opened a feature request on your behalf with Unplanned status. We prioritize our development based on customer demand, so I already registered your vote and you will receive notifications for any future updates. Let me know if you need more information. Regards, Apostolos
