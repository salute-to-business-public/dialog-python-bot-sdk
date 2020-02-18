# Changelog

## [Unreleased]
- Tests

## [3.0.0] - 2020-02-18
### Added
- AsyncTask (future)
- strict typing of input data
- Mapping from server's classes

### Changed
- All methods return AsyncTask with result
- All methods in Groups must get in Peer (group or group and privet) or AsyncTask with Group or Group and User(s)
- All methods where OutPeer was used replaced with Peer or AsyncTask (with Group/User)
- Peer now can get by creating the appropriate instance of the class
- All send methods return UUID
- All methods where date/seq was return now return None
- Docstrings
- example

### Removed
- Tests
- All methods which returned Peer/OutPeer without on_message
- send_audio
- send_video
- invite_users
- kick_users
