/*
 * View model for OctoPrint-FanSpeedMirror
 *
 * Author: Brad Morgan
 * License: AGPLv3
 */
$(function() {
    function FanSpeedMirrorViewModel(parameters) {
        var self = this;

		self.settings = parameters[0];
		self.control = parameters[1];
		self.loginState = parameters[2];

		self.settings.M106command = new ko.observable("");
		self.settings.m107command = new ko.observable("");

		self.updateSettings = function () {
			try {
				self.settings.M106command(self.settings.settings.plugins.FanSpeedMirror.M106command());
				self.settings.M107command(self.settings.settings.plugins.FanSpeedMirror.M107command());
			}
			catch (error) {
				console.log(error);
			}
		}

		//update settings in case user changes them, otherwise a refresh of the UI is required
		self.onSettingsHidden = function () {
			self.updateSettings();
		}
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: FanSpeedMirrorViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: ["loginStateViewModel", "settingsViewModel"],
        // Elements to bind to, e.g. #settings_plugin_FanSpeedMirror, #tab_plugin_FanSpeedMirror, ...
        elements: [ /* ... */ ]
    });
});
