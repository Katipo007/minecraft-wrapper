#Roadmap#
Here's a list of planned updates and the improvements that they may contain.

*Next Release (0.7.7? 0.8?)*
- Nothing yet

*Planned Changes*
- Dashboard changes [slated for 0.8+ only]:
  - Redesign interface (use SB-Admin 2.0 template as inspiration/base) and backend
    - Move over to websockets
    - Split multiple pages, use template system (possibly use Flask?)
  - Ability to modify server.properties with nice graphical settings
  - Rename files, edit text files, upload files, unzip/untar, etc. through file manager
  - Manage backups and backup settings through interface
    - Rollback to an existing backup with one click
    - Click button to force instant backup
    - See current backup status (and see when upcoming backup occurs)
  - Show faces in userlist without proxy mode, and cache locally
  - Update Wrapper.py with button, and see list of changes through interface
  - Real-time world map with players' positions and such
  - Move password from wrapper.properties to JSON storage. (and hash it, and allow for changing password from page itself and console)
  - View log files from server and wrapper
- Proxy changes:
  - Split proxy.py into four different files: __init__.py, server.py, client.py, and network.py
  - Split packet-handling methods into different functions for each protocol state (0, 1, 2, 3, etc.)
  - Support Forge 1.7.10 and Forge 1.8.x
  - Parse chunk packets, block packets, etc. and remember them for API usage
  - Proxy mode auto-mode when server-port and proxy-port are set to auto, for setup simplicity's sake. Automatically get server’s port, change it to something else, and then set the proxy-mode port to the server’s original port.
  - Allow connections without authentication in proxy-mode from other wrapper.py instances using player.connect() with an authentication key for the sake of having multiple servers without having to put the wrappers themselves all in offline mode
- Other changes:
  - "Sleep mode" for proxy mode, where server is -STOP'd to conserve CPU power when nobody is online
    - Alternative method that would work without proxy mode: Letting the server run, but limiting CPU power massively until someone logs in
  - Configuration system re-write (for wrapper.properties):
    - Re-write parser from scratch
    - Allow comments in the configuration file (wrapper.properties)
    - Make Config object __getattr__ capable, remove self.configManager in Wrapper object
  - Properly centralize UUID code - make a nice, centralized method of obtaining UUIDs regardless if proxy mode is enabled or not, and whether we're in offline more or not
 
#Next Update Discussion#
Would there be any need for a 0.7.8, or should we just start working on 0.8? 
Generally 0.x updates are massive, and I have a roadmap that I'm planning out 
for 0.8 but if I begin work on 0.8, I'd rather not have to worry about pushing 
any smaller updates (bug fixes or features) until 0.8 is done.

Discuss over at https://gitter.im/benbaptist/minecraft-wrapper .