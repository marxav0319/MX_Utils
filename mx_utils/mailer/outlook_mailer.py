"""
This is a programmatic outlook mailer implemented for the Windows operating system (tested on
Windows 10).  This may be expanded later but for now, Mac and *nix users will need to either write
a different mailer or potentially use a Windows virtual machine.

Author: Mark Xavier 
"""

from .base_mailer import Base_Mailer
import win32com.client as win32

class Outlook_Mailer(Base_Mailer):
    """
    A basic class that helps prepare and send, draft, or display an outlook mail item.  This is
    meant to be used for automated mailing.  It is important to note that none of this class'
    attributes are overwritten upon acting on the mail item (by saving, sending, or displaying).
    This means that one can technically call 'Outlook_Mailer.save_draft()' and then call
    'Outlook_Mailer.send()', and both will run seamlessly because the a separate object is created
    on each action call.  This means it's also possible to send the same message to the same user
    multiple times.
    """

    def __init__(self, recipients, subject, body, signature, cc_list=None, bcc_list=None,
                 attachments_list=None):
        """
        The initializer for the Outlook_Mailer object.

        Args:
            recipients <str>: The list of recipient emails to send to (separated by semicolons).
            subject <str>: The subject line of the email.
            body <str>: The HTML body of the email.
            signature <str>: The HTML signature of the email.
            cc_list <list : str>: A list of emails to cc separated by semicolons.
            bcc_list <list : str>: A list of emails to bcc separated by semicolons.
            attachments_list <list : str>: A list of filepaths to the attachments to include in the
                                           email.

        Returns:
            None
        """

        super().__init__(recipients, subject, body, signature)
        self.cc_list = cc_list
        self.bcc_list = bcc_list
        self.attachments_list = attachments_list
        self.application_dispatched = False
        self.email_object_prepared = False

    def _prepare_mail_item(self):
        """Prepares the email object in outlook given the initialized variables."""

        self.mail_object = self.application.CreateItem(0)
        self.mail_object.To = self.recipients
        self.mail_object.Subject = self.subject
        self.mail_object.CC = '' if self.cc_list == None else self.cc_list
        self.mail_object.BCC = '' if self.bcc_list == None else self.bcc_list
        self.mail_object.HTMLBody = '%s<br /><br />%s' % (self.body, self.signature)
        if self.attachments_list != None:
            for filepath in self.attachments_list:
                self.mail_object.Attachments.Add(filepath)

    def _dispatch_application_and_prepare_mail_item(self):
        """Dispatches the Outlook application and prepares the email object if not done."""

        # Dispatch application of not already dispatched.
        if not self.application_dispatched:
            self.application = win32.Dispatch('Outlook.Application')
            self.application_dispatched = True

        # Prepare the email object if it hasn't been prepared.
        if not self.email_object_prepared:
            self._prepare_mail_item()
            self.email_object_prepared = True

    def _reset_state(self):
        """
        Resets the state of the instance so that another email cannot be sent without updating
        the required instantiation fields.
        """

        self.recipients = None
        self.subjects = None
        self.body = None
        self.signature = None
        self.cc_list = None
        self.bcc_list = None
        self.attachments_list = None
        self.email_object_prepared = False

    def send(self, clear_state=True):
        """Sends the prepared email object."""

        self._dispatch_application_and_prepare_mail_item()
        self.mail_object.Send()
        if clear_state:
            self._reset_state()

    def save_draft(self, clear_state=True):
        """Saves the prepared email object in the drafts folder in Outlook."""

        self._dispatch_application_and_prepare_mail_item()
        self.mail_object.save()
        if clear_state:
            self._reset_state()

    def display_email(self, clear_state=True):
        """Displays the prepared email object to the user."""

        self._dispatch_application_and_prepare_mail_item()
        self.mail_object.Display(False)
        if clear_state:
            self._reset_state()
