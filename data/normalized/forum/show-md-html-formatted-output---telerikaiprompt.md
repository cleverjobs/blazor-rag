# Show MD/ HTML formatted output - TelerikAIPrompt

## Question

**Jus** asked on 24 Dec 2024

Hi, Is there any way to correctly display an HTML-formatted output using the TelerikAIPrompt control? The response I get from the API call is a Markdown string. I converted this to HTML, and all I see is text with the HTML tags printed (listed listed in the sample below). It would be nice to have a way to use (MarkupString) to ensure the HTML is correctly shown. My code is listed below for reference: @page "/aitest" @inject Microsoft.Extensions.Options.IOptions<ServerConfig> ServerConfig; @using Ganss.Xss; @using Markdig; @using Newtonsoft.Json.Linq; @using RestSharp; <TelerikAIPrompt OnPromptRequest="@HandlePromptRequest" @ref="@AIPromptRef"> </TelerikAIPrompt> @code { private TelerikAIPrompt AIPromptRef { get; set; }=default!; private async Task HandlePromptRequest(AIPromptPromptRequestEventArgs args) { string url="{url}"; var options=new RestClientOptions(url); var client=new RestClient(options); var request=new RestRequest("", Method.Post); request.AddHeader("Content-Type", "application/json"); request.AddJsonBody("{\"api_key\": \"" + ServerConfig.Value.APIKey.ToString() + "\", \"question\": \"" + args.Prompt + "\"}"); RestResponse response=new(); response=await client.PostAsync(request); JObject data=JObject.Parse(response.Content ?? string.Empty); var answer=data["answer"] switch { null=> string.Empty, _=> data["answer"]!.ToString() }; // Convert the Markdown in the output to HTML var pipeline=new MarkdownPipelineBuilder().UseAdvancedExtensions().Build(); string html=Markdown.ToHtml(answer, pipeline); // Sanitize the HTML var sanitizer=new HtmlSanitizer(); string safeHtml=sanitizer.Sanitize(html); args.Output=safeHtml; } }

## Answer

**Hristian Stefanov** answered on 24 Dec 2024

Hi Justin, To correctly display HTML-formatted output using the TelerikAIPrompt component, the recommended approach is to cast the sanitized HTML string to a MarkupString within the output view template. This will instruct Blazor to render it as HTML rather than plain text. Here’s an example I have prepared for you: <TelerikAIPrompt @ref="@AIPromptRef" OnPromptRequest="@HandlePromptRequest"> <AIPromptViews> <AIPromptPromptView ButtonText="Prompt View" ButtonIcon="@SvgIcon.Sparkles" /> <AIPromptOutputView ButtonText="Output View" ButtonIcon="@SvgIcon.Comment"> <ViewTemplate> @((MarkupString)(Output)) </ViewTemplate> </AIPromptOutputView> </AIPromptViews> </TelerikAIPrompt> @code {
private TelerikAIPrompt AIPromptRef { get; set; }
private string Output { get; set; }

private void HandlePromptRequest(AIPromptPromptRequestEventArgs args)
{
Output=" <strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </strong> ";
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Justin** commented on 24 Dec 2024

Hi Hristian, As always, thank you for the excellent support. That worked perfectly; I now have HTML-formatted output. Regards, Justin
