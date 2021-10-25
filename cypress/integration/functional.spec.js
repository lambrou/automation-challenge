describe('functional test', () => {
	const username = 'testqa1@testqa.com';
	const password = 'TestQA1!';
	const baseUrl = 'https://help.goboomtown.com/'
	it('can search for the word "customer"', () => {
		cy.visit(baseUrl);

		cy.intercept('POST', baseUrl).as('loginRequest');
		cy.get('a[id="login"]')
			.click();
		cy.get('div[id="loginWrapper"]')
			.should('not.have.attr', 'style', 'display:none;padding-right:5px');
		cy.get('input[name="email"]')
			.type(username)
			.should('have.value', username);
		cy.get('input[name="password"]')
			.type(password)
			.should('have.value', password);
		cy.get('form[id="login-form"]').submit();
		cy.wait('@loginRequest').then(({request}) => {
			expect(request.body).to.equal('email=testqa1%40testqa.com&password=TestQA1!');
		}).then(({response}) => {
			expect(response.body).to.have.property('success', true);
		});

		cy.get('input[id="search"]')
			.type('customer')
			.should('have.value', 'customer');

		cy.get('div[id="hasResults"]')
			.should('be.visible');
			
		cy.get('div[id="results"]')
			.find('div[class="topic-title"]')
			.each(div => {
				var title = div.find('h4').text();
				cy.visit(baseUrl + div.find('a').attr('href'));
				cy.get('h1')
					.first()
					.should('have.text', title);
				cy.wait(2000);
			})

		cy.visit(baseUrl)
	});
});