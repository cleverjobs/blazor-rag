# Additional horizontal scrollbar on top of grid

## Question

**Mar** asked on 30 Jun 2023

Hi, is it possible to achieve a result like in this dojo in blazor too? Greetings and thanks.

## Answer

**Hristian Stefanov** answered on 04 Jul 2023

Hi Marcus, I confirm that achieving the desired result with the Blazor Grid is indeed possible. To accomplish this, you can wrap the component in a div element that adds a top-side scrollbar. Additionally, you'll need to utilize a JavaScript function that synchronizes both scrollbars. To assist you further, I have prepared an example in this REPL link that showcases the outcome of implementing the approach mentioned above. I encourage you to run and test it to determine if it meets your requirements. If you encounter any challenges during the testing phase, I remain at your disposal. Regards, Hristian Stefanov

### Response

**Marcus** answered on 04 Jul 2023

Hi Hristian, first of all i want to thank you for the quick reply and the cleanup in the other support request. Said that i want to thank you for the nice solution. Basically it's working, but my case is a little bit more special. My users are able to resize the columns and then the scrollbar size no longer matches the size of the scrollbar at the bootom. In addition i was not able to set the scrollbar to 100% width to fit the table. Is it possible to adjust these points? Thanks in advance. Regards, Marcus

### Response

**Hristian Stefanov** commented on 07 Jul 2023

Hi Marcus, Thank you for getting back to me with feedback. I'm pleased to hear that you found the solution helpful. Based on your latest requirements, I have enhanced the solution to include automatic synchronization of scrollbar widths upon column resizing. This is achieved by introducing an additional JavaScript function that calculates the changed width and is triggered whenever a column resize occurs. I invite you to explore the upgraded example by following this REPL link. By running and testing it, you will notice that both scrollbars remain aligned as expected. If you have any further questions or need additional assistance, please feel free to reach out. Kind Regards, Hristian

### Response

**Marcus** answered on 03 Aug 2023

Hello Hristian, this works like a charm. The Scrollbar width is adjusted as desired. One last thing would make it perfect. I would like to have the scrollbar beneath my toolbar like in this REPL. Unfortunately it stops working if i try. Do you have a soultion to this too? Regards and thanks in advance. Marcus

### Response

**Hristian Stefanov** commented on 04 Aug 2023

Hi Marcus, I'm glad to see that the approach works well for you. Now let me help you enhance it so it fully matches your requirements. In order to keep the scrollbar working beneath the toolbar, incorporate to it a " display: block; " CSS style. For your convenience, I've made the necessary updates within the sample: REPL link. Please run and test it to see the result. Kind Regards, Hristian

### Response

**Marcus** answered on 07 Aug 2023

Hi Hristian, this works like a charm. Thank you very much. My request is finalized by your answer and the topic could be closed if possible. Regards, Marcus
