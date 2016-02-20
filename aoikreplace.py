#
import re

import sublime
import sublime_plugin


#
class AoikReplaceCommand(sublime_plugin.TextCommand):

    _MODE_V_REPLACE = 'replace'
    _MODE_V_TOGGLE = 'toggle'
    _MODE_V_S = (_MODE_V_REPLACE, _MODE_V_TOGGLE)

    def _get_regex(self, arg):
        """
        Get "regex" value from a dict or a string.

        @param arg: a dict or a string.

        If it is a dict, the format should be E.g.
        {
            "regex": "'",
            "value": "\""
        }
        The "regex" key's value is returned.

        If it is a string, the string is returned.
        """
        #
        if isinstance(arg, dict):
            regex = arg.get('regex', None)
        elif isinstance(arg, str):
            regex = arg
        else:
            assert 0, repr(arg)

        #
        return regex

    def _get_value(self, arg):
        """
        Get "value" value from a dict or a string.

        @param arg: a dict or a string.

        If it is a dict, the format should be like.
        {
            "regex": "'",
            "value": "\""
        }
        The "value" key's value is returned.

        If it is a string, the string is returned.
        """
        #
        if isinstance(arg, dict):
            value = arg.get('value', None)
        elif isinstance(arg, str):
            value = arg
        else:
            assert 0, repr(arg)

        #
        return value

    def run(self, edit, **args):
        """
        @param mode: a string:
        - 'replace': replace "src" regex pattern with "dst" replacement value.
          value.
        - 'toggle': replace "src" regex pattern with "dst" replacement value if
          "src" regex pattern is matched. Otherwise replace "dst" regex pattern
          with "src" replacement value.

        @param src: a regex pattern, or a replacement value.
        The value should be a dict or a string.

        If it is a dict, the format should be like.
        {
            // A regex pattern
            "regex": "'",
            // A replacement value
            "value": "\""
        }

        @param dst: a regex pattern, or a replacement value.
        The value should be a dict or a string.

        If it is a dict, the format should be like.
        {
            // A regex pattern
            "regex": "'",
            // A replacement value
            "value": "\""
        }
        """
        # Get argument "mode"
        mode = args.get('mode', None)

        # 4NAH9
        assert mode in self._MODE_V_S, \
            ("""Argument "mode"'s value "{}" is not one of {}.""")\
            .format(mode, self._MODE_V_S)

        # Get argument "src"
        src = args.get('src', None)

        assert src is not None, 'Argument "src" is missing.'

        # Get argument "dst"
        dst = args.get('dst', None)

        assert dst is not None, 'Argument "dst" is missing.'

        #
        window = sublime.active_window()

        if window is None:
            return

        #
        active_view = window.active_view()

        # Check if the selection is empty.
        # The selection is empty if all its regions are empty.
        selection_is_empty = all(x.empty() for x in active_view.sel())

        # If the selection is empty
        if selection_is_empty:
            # Select all text in the view.
            active_view.run_command('select_all')

        # Start to replace text in each region
        for region in reversed(active_view.sel()):
            # Reverse the regions to modify later regions first.

            # If the region is not empty
            if not region.empty():
                # Get the selected text
                text = active_view.substr(region)

                # Decide replacement "src" and "dst" according to "mode"
                if mode == self._MODE_V_REPLACE:
                    pass
                elif mode == self._MODE_V_TOGGLE:
                    #
                    src_regex = self._get_regex(src)

                    src_regex_is_matched = False

                    try:
                        src_regex_is_matched = bool(re.search(src_regex, text))
                    except re.error:
                        print(
                            'Src regex "{}" is invalid.'.format(src_regex))

                        return

                    #
                    dst_regex = self._get_regex(dst)

                    dst_regex_is_matched = False

                    try:
                        dst_regex_is_matched = bool(re.search(dst_regex, text))
                    except re.error:
                        print(
                            'Dst regex "{}" is invalid.'.format(dst_regex))

                        return

                    #
                    if src_regex_is_matched:
                        pass
                    elif dst_regex_is_matched:
                        # Switch "src" and "dst"
                        src, dst = dst, src
                    # If neither is matched in this region
                    else:
                        # Continue to process next region
                        continue

                # If any other "mode" value appears
                else:
                    # Ensured at 4NAH9
                    assert 0, repr(mode)

                # Replace the text
                try:
                    src_regex = self._get_regex(src)

                    dst_value = self._get_value(dst)

                    text = re.sub(src_regex, dst_value, text)
                except re.error:
                    print(
                        'Regex "{}" is invalid.'.format(src_regex))

                    return

                # Replace the selection with the new text
                active_view.replace(edit, region, text)
