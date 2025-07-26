# Telerik Grid when using AddInteractiveServerComponents - Can it be done?

## Question

**Mar** asked on 26 May 2024

DELETE THIS, DUMP QUESTION 😊 I have set render mode globally in App.razor <Routes @rendermode="InteractiveServer" /> <!DOCTYPE html> <html lang="en"> After I have done that, I get this error InvalidOperationException: A second operation was started on this context instance before a previous operation completed. This is usually caused by different threads concurrently using the same instance of DbContext. For more information on how to avoid threading issues with DbContext, see https: //go.microsoft.com/fwlink/?linkid=2097913. Microsoft.EntityFrameworkCore.Infrastructure.Internal.ConcurrencyDetector.EnterCriticalSection()
Microsoft.EntityFrameworkCore.Query.Internal.SingleQueryingEnumerable<T>+AsyncEnumerator.MoveNextAsync()
System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable<TResult>+ConfiguredValueTaskAwaiter.GetResult()
Microsoft.EntityFrameworkCore.EntityFrameworkQueryableExtensions.ToListAsync<TSource>(IQueryable<TSource> source, CancellationToken cancellationToken)
Microsoft.EntityFrameworkCore.EntityFrameworkQueryableExtensions.ToListAsync<TSource>(IQueryable<TSource> source, CancellationToken cancellationToken)
WhatsNew.Data.VersionRepository.GetApplicationsAsync() in VersionRepository.cs
+
{
_context=context;
} public async Task<List<Applications>> GetApplicationsAsync()
{ return await _context.Applications.ToListAsync();
} public async Task<Applications> GetApplicationByIdAsync ( int id ) { return await _context.Applications.FindAsync(id);
}
WhatsNew.Server.Components.Pages.ApplicationsPage.OnInitializedAsync() in ApplicationsPage.razor.cs
+ private List<Applications> applications=[]; private Applications selectedApplication=new (); private bool isEditMode; protected override async Task OnInitializedAsync () {
applications=await VersionRepository.GetApplicationsAsync();
} private void AddApplication () {
selectedApplication=new Applications();
isEditMode=true;
Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() This is how I register the repository builder.Services.AddTransient<IVersionRepository, VersionRepository>(); So, what am I doing wrong?
