import React from 'react';

import { EditorState, Modifier } from 'draft-js';
import PropTypes from 'prop-types';

// Creates the entities as soon as it is rendered.
class SansserifSource extends React.Component {
  componentDidMount() {
    const { editorState, entityType, onComplete } = this.props;

    const content = editorState.getCurrentContent();
    const selection = editorState.getSelection();

    // Gets the selected text from the editor
    var selectionState = editorState.getSelection();
    var anchorKey = selectionState.getAnchorKey();
    var currentContentBlock = content.getBlockForKey(anchorKey);
    var start = selectionState.getStartOffset();
    var end = selectionState.getEndOffset();
    var selectedText = currentContentBlock.getText().slice(start, end);

    // Uses the Draft.js API to create a new entity with the right data.
    const contentWithEntity = content.createEntity(
      entityType.type,
      'IMMUTABLE',
      {
        term: selectedText
      }
    );
    const entityKey = contentWithEntity.getLastCreatedEntityKey();

    // Add some text for the entity to be activated on.
    const text = `${selectedText}`;

    const newContent = Modifier.replaceText(
      content,
      selection,
      text,
      null,
      entityKey
    );
    const nextState = EditorState.push(
      editorState,
      newContent,
      'insert-characters'
    );

    onComplete(nextState);
  }

  render() {
    return null;
  }
}

SansserifSource.propTypes = {
  editorState: PropTypes.oneOfType([PropTypes.object, PropTypes.func]),
  entityType: PropTypes.oneOfType([PropTypes.object, PropTypes.func]),
  onComplete: PropTypes.oneOfType([PropTypes.object, PropTypes.func])
};

const Sansserif = ({ children }) => <span className="t-sans">{children}</span>;

Sansserif.propTypes = {
  children: PropTypes.oneOfType([
    PropTypes.array,
    PropTypes.element,
    PropTypes.func,
    PropTypes.object,
    PropTypes.string
  ])
};

export default {
  type: 'SANSSERIF',
  source: SansserifSource,
  decorator: Sansserif
};
