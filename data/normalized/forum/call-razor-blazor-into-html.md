# Call razor (blazor) into HTML

## Question

**Pet** asked on 08 Jan 2024

Hello, could you help me please. I have a problem with calling razor page (blazor) in HTML, sometime is work sometime isnt. I try call only [https://xzy.intra.cz/aktpoh/233](https://xzy.intra.cz/aktpoh/233) and press F5 and it was still working. But if I call it in iframe or embed or object i.e. <tr> <td>X group</td> <td><iframe href="[https://xzy.intra.cz/aktpoh/233"](https://xzy.intra.cz/aktpoh/233") height="50" type="text/html" width="300"></iframe></td> </tr> <tr> <td>Y group</td> <td><embed src="[https://xzy.intra.cz/aktpoh/30"](https://xzy.intra.cz/aktpoh/30") height="50" type="text/html" width="300"></embed></td> </tr> <tr> <td>Z group</td> <td><object data="[https://xzy.intra.cz/aktpoh/243"](https://xzy.intra.cz/aktpoh/243") height="50" type="text/html" width="300"></object></td> </tr> <tr> sometime work but if I press F5 for refresh sometime isnt work. How can I call it Peter

### Response

**Dimo** commented on 10 Jan 2024

Hi Peter. This question is not related to our components, so I will leave the thread open for the community to take part, if anyone has a suggestion. What I can say for sure is that iframes don't have a href attribute. They have a src attribute. The provided URLs don't seem to be valid, because they return 404.
