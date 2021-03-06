<sup>Copyright (C) 2016 - 2018 - BenBaptist and Wrapper.py developer(s).</sup>

# Welcome to the Wrapper.py Plugin API documentation! #

**The API is divided into modules.  Click on each module to see it's documentation**

 ##### [api/wrapperconfig](/documentation/wrapperconfig.rst)

 ##### [api/base](/documentation/base.rst)

 ##### [api/minecraft](/documentation/minecraft.rst)

 ##### [api/player](/documentation/player.rst)

 ##### [api/world](/documentation/world.rst)

 ##### [api/entity](/documentation/entity.rst)

 ##### [api/backups](/documentation/backups.rst)

 ##### [api/helpers](/documentation/helpers.rst)

<br>**Click here for a list of Wrapper's events**<br>[Wrapper.py Events](/documentation/events.rst)<br>

<br>


 **Looking for a specific method?  Look in this list to see which api module contains your desired method:** 

-  addGroupPerm -> [↩base](#apibase)
-  adjustBackupInterval -> [↩backups](#apibackups)
-  adjustBackupsKept -> [↩backups](#apibackups)
-  backupInProgress -> [↩backups](#apibackups)
-  backupIsIdle -> [↩backups](#apibackups)
-  banIp -> [↩minecraft](#apiminecraft)
-  banName -> [↩minecraft](#apiminecraft)
-  banUUID -> [↩minecraft](#apiminecraft)
-  blockForEvent -> [↩base](#apibase)
-  broadcast -> [↩minecraft](#apiminecraft)
-  callEvent -> [↩base](#apibase)
-  changeServerProps -> [↩minecraft](#apiminecraft)
-  chattocolorcodes -> [↩helpers](#apihelpers)
-  checkPassword -> [↩base](#apibase)
-  configWrapper -> [↩minecraft](#apiminecraft)
-  config_to_dict_read -> [↩helpers](#apihelpers)
-  config_write_from_dict -> [↩helpers](#apihelpers)
-  connect -> [↩player](#apiplayer)
-  console -> [↩minecraft](#apiminecraft)
-  countActiveEntities -> [↩entity](#apientity)
-  countEntitiesInPlayer -> [↩entity](#apientity)
-  createGroup -> [↩base](#apibase)
-  deOp -> [↩minecraft](#apiminecraft)
-  deleteGroup -> [↩base](#apibase)
-  deleteGroupPerm -> [↩base](#apibase)
-  disableBackups -> [↩backups](#apibackups)
-  enableBackups -> [↩backups](#apibackups)
-  epoch_to_timestr -> [↩helpers](#apihelpers)
-  execute -> [↩player](#apiplayer)
-  existsEntityByEID -> [↩entity](#apientity)
-  fill -> [↩world](#apiworld)
-  format_bytes -> [↩helpers](#apihelpers)
-  getAllPlayers -> [↩minecraft](#apiminecraft)
-  getBlock -> [↩world](#apiworld)
-  getClient -> [↩player](#apiplayer)
-  getDimension -> [↩player](#apiplayer)
-  getEntityByEID -> [↩entity](#apientity)
-  getEntityControl -> [↩minecraft](#apiminecraft)
-  getEntityInfo -> [↩entity](#apientity)
-  getFirstLogin -> [↩player](#apiplayer)
-  getGameRules -> [↩minecraft](#apiminecraft)
-  getGamemode -> [↩player](#apiplayer)
-  getGroups -> [↩player](#apiplayer)
-  getHeldItem -> [↩player](#apiplayer)
-  getItemInSlot -> [↩player](#apiplayer)
-  getLevelInfo -> [↩minecraft](#apiminecraft)
-  getOfflineUUID -> [↩minecraft](#apiminecraft)
-  getPlayer -> [↩minecraft](#apiminecraft)
-  getPlayers -> [↩minecraft](#apiminecraft)
-  getPluginContext -> [↩base](#apibase)
-  getPosition -> [↩player](#apiplayer)
-  getServer -> [↩minecraft](#apiminecraft)
-  getServerPackets -> [↩minecraft](#apiminecraft)
-  getServerPath -> [↩minecraft](#apiminecraft)
-  getSpawnPoint -> [↩minecraft](#apiminecraft)
-  getStorage -> [↩base](#apibase)
-  getTime -> [↩minecraft](#apiminecraft)
-  getTimeofDay -> [↩minecraft](#apiminecraft)
-  getUuidCache -> [↩minecraft](#apiminecraft)
-  getWorld -> [↩minecraft](#apiminecraft)
-  getWorldName -> [↩minecraft](#apiminecraft)
-  get_int -> [↩helpers](#apihelpers)
-  getargs -> [↩helpers](#apihelpers)
-  getargsafter -> [↩helpers](#apihelpers)
-  getfileaslines -> [↩helpers](#apihelpers)
-  getjsonfile -> [↩helpers](#apihelpers)
-  getplayerby_eid -> [↩minecraft](#apiminecraft)
-  giveStatusEffect -> [↩minecraft](#apiminecraft)
-  hasGroup -> [↩player](#apiplayer)
-  hasPermission -> [↩player](#apiplayer)
-  hashPassword -> [↩base](#apibase)
-  isIpBanned -> [↩minecraft](#apiminecraft)
-  isOp -> [↩player](#apiplayer)
-  isServerStarted -> [↩minecraft](#apiminecraft)
-  isUUIDBanned -> [↩minecraft](#apiminecraft)
-  isipv4address -> [↩helpers](#apihelpers)
-  kick -> [↩player](#apiplayer)
-  killEntityByEID -> [↩entity](#apientity)
-  lookupUUID -> [↩minecraft](#apiminecraft)
-  lookupbyName -> [↩minecraft](#apiminecraft)
-  lookupbyUUID -> [↩minecraft](#apiminecraft)
-  makeOp -> [↩minecraft](#apiminecraft)
-  message -> [↩minecraft](#apiminecraft)
-  message -> [↩player](#apiplayer)
-  mkdir_p -> [↩helpers](#apihelpers)
-  openWindow -> [↩player](#apiplayer)
-  pardonIp -> [↩minecraft](#apiminecraft)
-  pardonName -> [↩minecraft](#apiminecraft)
-  pardonUUID -> [↩minecraft](#apiminecraft)
-  performBackup -> [↩backups](#apibackups)
-  pickle_load -> [↩helpers](#apihelpers)
-  pickle_save -> [↩helpers](#apihelpers)
-  processcolorcodes -> [↩helpers](#apihelpers)
-  processoldcolorcodes -> [↩helpers](#apihelpers)
-  pruneBackups -> [↩backups](#apibackups)
-  putjsonfile -> [↩helpers](#apihelpers)
-  read_timestr -> [↩helpers](#apihelpers)
-  readout -> [↩helpers](#apihelpers)
-  refreshOpsList -> [↩minecraft](#apiminecraft)
-  registerCommand -> [↩base](#apibase)
-  registerEvent -> [↩base](#apibase)
-  registerHelp -> [↩base](#apibase)
-  registerPermission -> [↩base](#apibase)
-  removeGroup -> [↩player](#apiplayer)
-  removePermission -> [↩player](#apiplayer)
-  replace -> [↩world](#apiworld)
-  resetGroups -> [↩base](#apibase)
-  resetPerms -> [↩player](#apiplayer)
-  resetUsers -> [↩base](#apibase)
-  say -> [↩player](#apiplayer)
-  scrub_item_value -> [↩helpers](#apihelpers)
-  sendAlerts -> [↩base](#apibase)
-  sendBlock -> [↩player](#apiplayer)
-  sendCommand -> [↩player](#apiplayer)
-  sendEmail -> [↩base](#apibase)
-  setBlock -> [↩minecraft](#apiminecraft)
-  setChunk -> [↩world](#apiworld)
-  setGamemode -> [↩player](#apiplayer)
-  setGroup -> [↩player](#apiplayer)
-  setLocalName -> [↩minecraft](#apiminecraft)
-  setPermission -> [↩player](#apiplayer)
-  setPlayerAbilities -> [↩player](#apiplayer)
-  setResourcePack -> [↩player](#apiplayer)
-  setVisualXP -> [↩player](#apiplayer)
-  set_item -> [↩helpers](#apihelpers)
-  summonEntity -> [↩minecraft](#apiminecraft)
-  teleportAllEntities -> [↩minecraft](#apiminecraft)
-  uuid -> [↩player](#apiplayer)
-  verifyTarInstalled -> [↩backups](#apibackups)
-  wrapperHalt -> [↩base](#apibase)