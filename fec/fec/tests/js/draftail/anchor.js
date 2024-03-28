import React from 'react';
import { expect } from 'chai';
import { EditorState } from 'draft-js';

import './setup.js';
import { shallow } from 'enzyme';

import { default as Anchor } from '../../../static/js/draftail/Anchor.js';

describe('draftail - Anchor Block Component', function() {
  it('should build a Anchor object for Draftail to consume', function() {
    expect(Anchor).to.be.an('object');
    expect(Anchor).to.have.keys('type', 'source', 'decorator');
    expect(Anchor.type).to.equal('ANCHOR');
  });

  it('the Anchor decorator should build a react element', function() {
    var Decorator = Anchor.decorator;
    var element = shallow(<Decorator>test</Decorator>);
    expect(element.childAt(0).text()).to.equal('test');
    expect(element.type()).to.equal('span');
  });

  it('the Anchor source should build an anchor component from selected text', function(done) {
    var Source = Anchor.source;
    var editorState = EditorState.createEmpty();
    var entityType = editorState.getCurrentContent().createEntity();
    var onComplete = function(next) {
      expect(next).to.be.an('object');
      done();
    };
    var element = shallow(<Source editorState={editorState} entityType={entityType} onComplete={onComplete} />);
  });
});
