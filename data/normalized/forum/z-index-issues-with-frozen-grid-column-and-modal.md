# Z-index issues with Frozen grid column and modal

## Question

**Adr** asked on 29 Jun 2021

I am having an issue with my z-index, then freezing grid columns. There are obviously then becoming sticky, which creates a new stacking context, and sticks to the nearest ancestor? I think this may be where the problem lies. As a result when my fixed modal is activated this happens, and I just can't seem to fix the problem. Any ideas? Thank you!

## Answer

**Marin Bratanov** answered on 29 Jun 2021

Hello Adrian, Can you reproduce this problem with the sample I am attaching here? If not, does comparing against it help you solve it? Perhaps the key thing is where you have the TelerikRootComponent defined - it needs to be high in the DOM hierarchy so popups can appear above other elements. You can read more about it here. Regards, Marin Bratanov Progress Telerik

### Response

**Adrian** commented on 02 Jul 2021

Hi Marin Thank you for your help, your TelerikBlazorApp1, helped me solve the issue. Many Thanks

### Response

**Marin Bratanov** commented on 03 Jul 2021

I'm glad you solved it :)
