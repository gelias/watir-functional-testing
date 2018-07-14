require 'rubygems'
require 'watir'
require 'rspec'

describe "Look for browser elements" do

    before(:each) {
        @browser = Watir::Browser.start 'https://docs.google.com/forms/d/e/1FAIpQLSd62UwIUW8MwqwnUo-yNH8v3RLMXKnPHIl68EUtTALkdu12kg/viewform'
    }

	it "Should check email address text field" do
		text_field = @browser.text_field name: 'emailAddress'
        expect(true).to be(text_field.exists?)
    end

    it "Should fill email address" do
        email_address = 'guilherme.elias@gmail.com'
		text_field = @browser.text_field name: 'emailAddress'
        text_field.set email_address
        expect(email_address).to eq(text_field.value)
    end
 
    after(:each) {}

end
