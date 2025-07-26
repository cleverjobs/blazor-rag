# Blazor LoaderContainer and Loader not being announced by screen readers

## Question

**Ric** asked on 21 Jun 2022

Hello, I'm trying to comply with accessibility standards and I'm unable to get the Loader text to be read by screen readers. I've tried wrapping the Loader component in an aria-live element, using templates, and even loaded up your GitHub loader examples to no avail. Can you shed some light on what may potentially be happening and how to get it picked up by the screen readers? Thanks

### Response

**Hristian Stefanov** commented on 24 Jun 2022

Hi Rick, I'm pasting the reply I gave in the other ticket for the same question here:===I'm ready to help out. Now let's first cover some additional questions that appear in my mind based on the described situation below. What is the used screen reader that shows a problem reading the text of the loader? What is the used browser? What is the configuration? Such information will help me understand the scenario better. I tried to reproduce the described behavior by creating a small example and testing it with the NVDA screen reader: <div class="loader-container"> <span class="loader-size-title"> MyLoader </span> <TelerikLoader Class="loader-indicator" Type="@LoaderType.InfiniteSpinner" Size="@(ThemeConstants.Loader.Size.Medium)"> </TelerikLoader> </div> @code {
} <style>.loader-size-title { display: block; margin-bottom: 10px;
}.loader-container { text-align: center; width: 150px; display: inline-table; padding-top: 10px;
} </style> As a result, the NVDA seems to read correctly the loader text. Please run and test to see if the result you get is the same. I look forward to your reply.===Let's continue the conversation in the public post for better visibility. Thank you.
