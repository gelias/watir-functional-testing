require 'rubygems'
require 'watir'
require 'rspec'

describe "Take a look on login screen" do

    before(:each) {
        @browser = Watir::Browser.start 'https://center.umov.me'
        @workspace_field = @browser.text_field name: 'authorization.workspace'
        @username_field = @browser.text_field name: 'authorization.username'
        @password_field = @browser.text_field name: 'authorization.password'
    }

	it "Should get an error when workspace does not exist" do
        @workspace_field.set 'unknown'
        @username_field.set 'user'
        @password_field.set 'mypass'
        login_button = @browser.button id: 'submit_button'
        login_button.exist?
        login_button.click
        error_msg = @browser.span class: 'nm-text'
        expect('THE COMPANY DOES NOT EXISTS.').to eq(error_msg.text)
    end

    it "Should get an error when recaptcha is enable but does not used alias" do
        @workspace_field.set 'elias'
        @username_field.set 'user'
        @password_field.set 'mypass'
        login_button = @browser.button id: 'submit_button'
        login_button.exist?
        login_button.click
        error_msg = @browser.span class: 'nm-text'
        expect('WRONG RECAPTCHA VALIDATION!').to eq(error_msg.text)
    end
    
    after(:each) {
        @browser.close
    }

end
