    </div>
  </main>
  <footer class="mt-4">
    <div class="container p-1">
      <p class="x-small text-end"><%= $tPoweredBy %> <a href="https://github.com/OpenIPC/microbe-web">Microbe Web UI</a>, <%= $tPartOf %> <a href="https://openipc.org/">OpenIPC project</a>.</p>
    </div>
  </footer>
<% if [ "$debug" -ge "1" ]; then %>
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasDebug" aria-labelledby="offcanvasDebugLabel">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasDebugLabel">Debug Info</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body x-small">
      <p><a class="btn btn-warning" href="webui-init.cgi">Refresh Environment</a></p>
      <% ex env | sort %>
      <% ex "cat /tmp/sysinfo.txt" %>
    </div>
  </div>
  <button type="button" class="btn btn-primary fixed-bottom" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDebug" aria-controls="offcanvasDebug">Debug</button>
<% fi %>
</body>
</html>
