# How to setup Blazor server app to call api in same project?

## Question

**Bit** asked on 19 Jun 2020

Im using a code-behind approach as in this article [https://www.telerik.com/blogs/using-a-code-behind-approach-to-blazor-components](https://www.telerik.com/blogs/using-a-code-behind-approach-to-blazor-components) When using the upload component, we need to specify a SaveUrl [https://docs.telerik.com/blazor-ui/components/upload/overview](https://docs.telerik.com/blazor-ui/components/upload/overview) Is that the only way? Can we have a web api that and a blazor server app in the same project, with the api handlers handling routes also?

## Answer

**Marin Bratanov** answered on 19 Jun 2020

Hi, The Upload component needs a SaveUrl so it knows where to send the file. That URL can be in the same project, or in another project, or even on another server, this is entirely up to your needs. It can be WebAPI, it can be ASP.NET Classic, ASP.NET Core, or any other suitable service that accepts files. You can have WebAPI controllers in a server-side Blazor project, too, you can find an example of this in our demos solution that you can find in the "demos" folder of your installation - it has Upload demos that point to a controller in the same project. Regards, Marin Bratanov

### Response

**BitShift** answered on 19 Jun 2020

Ok, I thought so. Wheew, I was worried for a min. Really didnt want to setup a seperate api project. I'm pretty sure I had done this before and it was working, but ive since lost that code. I'm off to look at that demo code.

### Response

**BitShift** answered on 19 Jun 2020

Ended up being a 401 issue, which I found with Fiddler. Something wasnt right. Had to add a few more options in Startup since Im using windows auth.
