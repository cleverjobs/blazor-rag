# Media Query doesn't work on iPhone

## Question

**Cip** asked on 20 Aug 2022

Hi everyone, I've tried to use the Media Query Component, and it worked and all was fine in Chrome on the simulator, also on Android Devices, but when I arrived to test the design on iPhone that didn't work. Then I belived that maybe it's Safari the problem and I downloaded Chrome on iPhone, but I had the same issue on Chrome too. I don't know how to solve it, maybe if I will try from CSS directly to solve it will work. I have checked the viewport meta tag, I believed that was missing, but no, it was there in the _Host.cshtml file. Does anyone encountered this issue till now? My app is a Server Side Blazor app. Thank you in advance. Best regards, Cipri

### Response

**Robert C** commented on 20 Aug 2022

I am doing the same and it works for me in my Server project. I also shipped my app using Maui (Blazor Hybrid) and it works on iPhone just fine. Please post your Media Query related code.

### Response

**Ciprian Daniel** commented on 23 Aug 2022

Hi Robert, You were right. I checked my Media Queries and I have figured out that I have made some mistakes over there. The "or" word doesn't exists, I replaced it with comma, and now everything works fine. Thank you for your help.
