# Access Grouping value in GroupFooterTemplate within a Grid

## Question

**Ben** asked on 28 May 2021

Hello together I have a hopefully simple question. How can I access the grouping value in the GroupFooterTemplate? What I can do in the GroupHeaderTemplate by using context.Value in the GroupFooterTemplate only aggregations are given in the "context". Any help apreciated. Best regards, Benjamin

## Answer

**Marin Bratanov** answered on 28 May 2021

Hello again Benjamin, I just realized I had missed a key point in your question. You are correct, the group footer does not provide the current group value, and just storing it from the header won't work out because there can be multiple groups. So, for this you would need the template to provide more info in the context and that's something we need to implement in the component. You can Follow its status here: [https://feedback.telerik.com/blazor/1486405-expose-current-group-field-value-and-the-rest-of-the-field-aggregates-in-the-groupfootertemplate.](https://feedback.telerik.com/blazor/1486405-expose-current-group-field-value-and-the-rest-of-the-field-aggregates-in-the-groupfootertemplate.) I've added your Vote to it on your behalf to raise its priority, and if you click the Follow button you will start getting emails for status updates (such as when we know which release will have it). Regards, Marin Bratanov Progress Telerik

### Response

**Ecofip** commented on 21 Apr 2022

Hello Marin, we faced the same problem in our project, so I up-voted the "issue" you linked. I wrote down a comment in order to point out the fact that this functionality seems available in the JQuery Kendo version. Do you think I can do anything else to help this functionality be implemented? I see that the project is not open source, but maybe I am wrong and we can develop a Pull Request to do so? Thanks, Dylan

### Response

**Marin Bratanov** commented on 23 Apr 2022

Thank you for the offer, but at this point I can't say there is a well devised and official way to accept such contributions (as you well noted, this is not OSS). Without such a formal process, I'd expect that working through those kinks will take more time than implementing it ourselves would. Nevertheless, if you are willing to do the legwork, you can download the source code from your account and tweak it. You could then send us the modified version in a private support ticket and, who knows, something may work out. I must add a few disclaimers, though: 1) we do not support modified versions of our software and 2) that suggestion is in no way binding and I cannot promise anything would come out of such an endeavor. I am sorry to be the bearer of bad news, but I thought it best to be fully open and honest.

### Response

**Ecofip** commented on 25 Apr 2022

Thanks for the explanation Marin, it gives us some interesting information! (and I prefer 1000 times your approach, being honest and direct, than talking with vague words or anything, so thanks for that too :) )

### Response

**Marin Bratanov** commented on 25 Apr 2022

You're most welcome!

### Response

**Marin Bratanov** answered on 28 May 2021

Hello Benjamin, You can take the value from the context and store it in a field in your view-model so you can use it for other things. Regards, Marin Bratanov Progress Telerik
