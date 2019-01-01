/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	config.language = 'ko';
	// config.uiColor = '#AADC6E';
	config.width: '100%';
    config.height: 400;
    config.extraPlugins = 'bootstrapVisibility','imageresponsive','image2','emoji','codesnippet','pastefromword';
    config.filebrowserUploadMethod = 'form';

};

