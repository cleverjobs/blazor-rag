# UpdateHandler does not get triggered when entering first value in grid

## Question

**Mir** asked on 13 Nov 2020

Hi, now I discovered another Problem depending on my last Thread: [https://www.telerik.com/forums/avoid-multiple-calls-of-async-updatehandler-when-pressing-enter](https://www.telerik.com/forums/avoid-multiple-calls-of-async-updatehandler-when-pressing-enter) Your solution works fine as long as I do not enter the very first value in my grid and it makes no difference which row is changed. When I enter the first value then the UpdateHandler does not get triggered. Only my ChangeHandler. Do you have an idea why this is happening?

## Answer

**Joana** answered on 13 Nov 2020

Hello Miriam, I just replied in your current thread regarding the UpdateHandler. I am pasting the reply here for your convenience, and I suggest that we continue the communication in a single thread: It seems that I have missed this when I was testing the solution. My apologies for that. The issue stems from the default value of the flag that we created for this case. public bool ShouldUpdateItem { get; set; }=true; ShouldUpdateItem default value should be true, to accept the first call of the Update handler. I hope this will fullfil your scenario. Let me know if I could help you further. Regards, Joana

### Response

**Miriam** answered on 15 Nov 2020

Hi, thank you very much!
