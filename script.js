import React from 'react';

class App extends React.Component {
	constructor() {
		super();
		this.state = {
			baseURI: ''
		}
	}
	retrievaAPIResults(url) {
		fetch(url)
			.then(function(response) {
				
			})
	}
	render () {
		return (
			<p>Hello</p>
		);
	}
}